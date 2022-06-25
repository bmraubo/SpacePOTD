import logging

class ImageService:
    def __init__(self, api_client):
        logging.info("Starting Image Service")
        self.api_client = api_client

    def get_data(self):
        logging.info("Fetching image data")
        response_json = self.api_client.get_data()
        return {
            "name": response_json["title"],
            "date": response_json["date"],
            "url": response_json["url"],
        }
        