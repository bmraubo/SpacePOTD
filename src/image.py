import requests
import logging
from io import BytesIO


class Image:
    data = None
    ready = False

    def __init__(self, nasa_api_data):
        self.name = nasa_api_data["name"]
        self.date = nasa_api_data["date"]
        self.url = nasa_api_data["url"]

    def fetch_image(self):
        logging.info("fetching image")
        try:
            response = requests.get(self.url)
            self.data = BytesIO(response.content)
            self.ready = True
        except:
            logging.error("failed to fetch image")

    def has_been_posted(self, last_posted_image_date):
        return (
            False
            if last_posted_image_date == None
            else self.date == last_posted_image_date
        )

    def build_json(self):
        return {"name": self.name, "date": self.date, "url": self.url}
