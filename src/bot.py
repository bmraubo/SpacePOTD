import requests
import time
from io import BytesIO

class Bot:
    wait_time = 10800
    
    def __init__(self, nasa_connect, twitter_connect):
        self.nasa_connect = nasa_connect
        self.twitter_connect = twitter_connect

    def prepare_image(self, image_url):
        try:
            response = requests.get(image_url)
            self.image = BytesIO(response.content)
            self.image_ready = True
        except:
            self.image_ready = False

    def post_image(self, data):
        image_name = data["title"]
        image_url = data["url"]
        date = data["date"]
        print("New Image - Posting")
        self.prepare_image(image_url)
        if self.image_ready:
            media_upload_response = self.twitter_connect.upload_media(image_name, self.image)
            media_id = media_upload_response.media_id
            post_response = self.twitter_connect.post_text_with_image(image_name, media_id)
            self.last_post_id = post_response._json["id"]
            self.set_last_posted_image_date(date)
            print("Image Posted")
            return True
        else:
            return False

    def get_image_data(self):
        print("Contacting NASA API")
        return self.nasa_connect.get_data()

    def set_last_posted_image_date(self, posted_image_date):
        self.last_posted_image_date = posted_image_date

    def posted_on_date(self, new_date):
        try:
            return self.last_posted_image_date == new_date
        except AttributeError:
            return False

    def wait(self):
        print("Waiting")
        time.sleep(self.wait_time)
    
    def start(self):
        print("Bot is starting")
        while True:
            nasa_api_response = self.get_image_data()
            print(f"NASA API Response:\nTitle:{nasa_api_response['title']}\nDate:{nasa_api_response['date']}\nUrl:{nasa_api_response['url']}")
            if not self.posted_on_date(nasa_api_response["date"]):
                self.post_image(nasa_api_response)
                self.wait()
            else:
                print("This image has already been posted")
                self.wait()

