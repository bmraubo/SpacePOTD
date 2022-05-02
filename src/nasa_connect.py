import requests
from .settings import NASA_API_KEY

class NasaConnect:
    base_url = "https://api.nasa.gov/planetary/apod"
    api_key = NASA_API_KEY
    
    def get_data(self):
        print(self.api_key)
        return requests.get(self.base_url, params= {"api_key": self.api_key})