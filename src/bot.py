import time
import logging
from .image import Image


class Bot:
    wait_time = 10800

    def __init__(self, nasa_connect, twitter_connect, storage):
        self.nasa_connect = nasa_connect
        self.twitter_connect = twitter_connect
        self.storage = storage

    def get_image_data(self):
        return self.nasa_connect.get_data()

    def upload_media(self, image):
        media_upload_response = self.twitter_connect.upload_media(
            image.name, image.file
        )
        return media_upload_response.media_id

    def post_image(self, image):
        logging.info("New Image - Posting")
        image.fetch_image()
        if image.ready:
            media_id = self.upload_media(image)
            post_response = self.twitter_connect.post_text_with_image(
                image.name, media_id
            )
            self.last_post_id = post_response._json["id"]
            logging.info("Image Posted")
            self.storage.add_image(image)
            return True
        else:
            return False

    def respond_with_description(self, image):
        try:
            self.twitter_connect.respond_with_text(image.description, self.last_post_id)
            return True
        except Exception as e:
            logging.critical(e)
            return False

    def wait(self):
        logging.info("waiting...")
        time.sleep(self.wait_time)

    def start(self):
        logging.info("Bot is Starting")
        while True:
            nasa_api_response = self.get_image_data()
            image = Image(nasa_api_response)
            last_image = self.storage.get_last_image()
            if not image.has_been_posted(last_image.date):
                self.post_image(image)
                self.wait()
            else:
                logging.info("Image has already been posted")
                self.wait()
