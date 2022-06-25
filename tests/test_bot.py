from .mocks import MockNasaApiClient, MockTwitterApiClient
from src.nasa_connect import NasaConnect
from src.twitter_connect import PostingService
from src.storage import Storage
from src.bot import Bot
from src.image import Image
from os.path import join
import json

MOCK_NASA_API_DATA = {
    "copyright": "Aixa Andrada",
    "date": "2022-05-02",
    "explanation": "An Explanation",
    "hdurl": "https://apod.nasa.gov/apod/image/2205/PartialEclipse_Andrada_2048.jpg",
    "media_type": "image",
    "service_version": "v1",
    "title": "Partial Solar Eclipse over Argentina",
    "url": "https://apod.nasa.gov/apod/image/2205/PartialEclipse_Andrada_960.jpg",
}

history_file = join("tests", "mock_history.txt")


def set_up_bot():
    nasa_client = MockNasaApiClient()
    nasa_connect = NasaConnect(nasa_client)
    twitter_client = MockTwitterApiClient()
    twitter_connect = PostingService(twitter_client)
    storage = Storage(history_file)
    bot = Bot(nasa_connect, twitter_connect, storage)
    return bot


def reset_history_file():
    data = [{"name": "Image Name", "date": "1111-11-11", "url": "www.example.com"}]
    with open(history_file, "w") as file:
        data_string = json.dumps(data)
        file.write(data_string)


def test_bot_can_post_an_image():
    bot = set_up_bot()
    image = Image(bot.nasa_connect.get_data())
    image_posted = bot.post_image(image)
    assert image_posted == True
    assert image.build_json() in bot.storage.data
    bot.twitter_connect.delete_tweet(bot.last_post_id)
    reset_history_file()
