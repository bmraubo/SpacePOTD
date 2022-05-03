import time
from .image import Image


class Bot:
    wait_time = 10800

    def __init__(self, nasa_connect, twitter_connect):
        self.nasa_connect = nasa_connect
        self.twitter_connect = twitter_connect

    def get_image_data(self):
        print("Contacting NASA API")
        return self.nasa_connect.get_data()

    def upload_media(self, image):
        media_upload_response = self.twitter_connect.upload_media(
            image.name, image.file
        )
        return media_upload_response.media_id

    def post_image(self, image):
        print("New Image - Posting")
        image.fetch_image()
        if image.ready:
            media_id = self.upload_media(image)
            post_response = self.twitter_connect.post_text_with_image(
                image.name, media_id
            )
            self.last_post_id = post_response._json["id"]
            self.set_last_posted_image_date(image.date)
            print("Image Posted")
            return True
        else:
            return False

    def set_last_posted_image_date(self, posted_image_date):
        self.last_posted_image_date = posted_image_date

    def wait(self):
        print("Waiting")
        time.sleep(self.wait_time)

    def start(self):
        print("Bot is starting")
        while True:
            nasa_api_response = self.get_image_data()
            image = Image(nasa_api_response)
            if not image.has_been_posted(self.last_posted_image_date):
                self.post_image(image)
                self.wait()
            else:
                print("This image has already been posted")
                self.wait()
