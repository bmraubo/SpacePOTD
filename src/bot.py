import requests
from io import BytesIO

class Bot:
    
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
