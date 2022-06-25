import time
import logging


class Bot:
    wait_time = 10800

    def __init__(self, image_service, posting_service, storage):
        self.image_service = image_service
        self.posting_service = posting_service
        self.storage = storage

    def get_image_data(self):
        return self.image_service.fetch_image()

    def upload_media(self, image):
        media_upload_response = self.posting_service.upload_media(
            image.name, image.data
        )
        return media_upload_response.media_id

    def post_image(self, image):
        logging.info("New Image - Posting")
        if image.ready:
            media_id = self.upload_media(image)
            post_response = self.posting_service.post_text_with_image(
                image.name, media_id
            )
            self.last_post_id = post_response._json["id"]
            logging.info("Image Posted")
            self.storage.add_image(image)
            return True
        else:
            return False

    def wait(self):
        logging.info("waiting...")
        time.sleep(self.wait_time)

    def start(self):
        logging.info("Bot is Starting")
        while True:
            image = self.get_image_data()
            last_image = self.storage.get_last_image()
            if not image.has_been_posted(last_image.date):
                self.post_image(image)
                self.wait()
            else:
                logging.info("Image has already been posted")
                self.wait()
