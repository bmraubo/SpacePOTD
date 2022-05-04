import requests
from .settings import NASA_API_KEY


class NasaConnect:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_data(self):
        response_json = self.api_client.get_data()
        return {
            "name": response_json["title"],
            "date": response_json["date"],
            "url": response_json["url"],
        }


class NasaApiClient:
    base_url = "https://api.nasa.gov/planetary/apod"
    api_key = NASA_API_KEY

    def get_data(self):
        response = requests.get(self.base_url, params={"api_key": self.api_key})
        return response.json()
