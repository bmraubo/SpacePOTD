import logging

from src.image import Image

class ImageService:
    def __init__(self, api_client):
        logging.info("Starting Image Service")
        self.api_client = api_client

    def fetch_image(self):
        api_data = self.get_api_data()
        image = Image(api_data)
        image.fetch_image()
        return image

    def get_api_data(self):
        logging.info("Fetching image data")
        response_json = self.api_client.get_data()
        return {
            "name": response_json["title"],
            "date": response_json["date"],
            "url": response_json["url"],
        }
        