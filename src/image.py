import requests
from io import BytesIO


class Image:
    image_ready = False

    def __init__(self, nasa_api_data):
        self.name = nasa_api_data["title"]
        self.date = nasa_api_data["date"]
        self.url = nasa_api_data["url"]

    def fetch_image(self):
        try:
            response = requests.get(self.url)
            self.image = BytesIO(response.content)
            self.image_ready = True
        except:
            print("Failed to fetch image")
