from .mocks import MockNasaApiClient
from src.nasa_connect import NasaConnect
from src.twitter_connect import TwitterConnect
from src.bot import Bot

def test_bot_can_prepare_image_for_upload():
    image_url = "https://apod.nasa.gov/apod/image/2205/PartialEclipse_Andrada_960.jpg"
    nasa_api_client = MockNasaApiClient()
    nasa_connect = NasaConnect(nasa_api_client)
    twitter_connect = TwitterConnect()
    bot = Bot(nasa_connect, twitter_connect)
    bot.prepare_image(image_url)
    assert bot.image != None
    assert bot.image_ready == True

def test_bot_can_post_an_image():
    nasa_api_client = MockNasaApiClient()
    nasa_connect = NasaConnect(nasa_api_client)
    twitter_connect = TwitterConnect()
    bot = Bot(nasa_connect, twitter_connect)
    data = bot.nasa_connect.get_data()
    image_posted = bot.post_image(data)
    assert image_posted == True
    bot.twitter_connect.delete_tweet(bot.last_post_id)

def test_bot_can_compare_dates():
    date = "2022-05-02"
    nasa_api_client = MockNasaApiClient()
    nasa_connect = NasaConnect(nasa_api_client)
    twitter_connect = TwitterConnect()
    bot = Bot(nasa_connect, twitter_connect)
    bot.set_last_posted_image_date(date)
    assert bot.posted_on_date(date) == True

def test_bot_can_compare_dates_where_last_posted_date_is_none():
    date = "2022-05-02"
    nasa_api_client = MockNasaApiClient()
    nasa_connect = NasaConnect(nasa_api_client)
    twitter_connect = TwitterConnect()
    bot = Bot(nasa_connect, twitter_connect)
    assert bot.posted_on_date(date) == False

