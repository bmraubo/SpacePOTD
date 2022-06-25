import requests
import logging
from ..settings import NASA_API_KEY

class NasaAPIClient:
    base_url = "https://api.nasa.gov/planetary/apod"
    api_key = NASA_API_KEY

    def get_data(self):
        logging.info("Contacting NASA API")
        response = requests.get(self.base_url, params={"api_key": self.api_key})
        return response.json()
        