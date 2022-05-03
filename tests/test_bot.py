from .mocks import MockNasaApiClient
from src.twitter_connect import TwitterConnect
from src.bot import Bot

def test_bot_can_prepare_image_for_upload():
    image_url = "https://apod.nasa.gov/apod/image/2205/PartialEclipse_Andrada_960.jpg"
    nasa_connect = MockNasaApiClient()
    twitter_connect = TwitterConnect()
    bot = Bot(nasa_connect, twitter_connect)
    bot.prepare_image(image_url)
    assert bot.image != None
    assert bot.image_ready == True