from email.mime import image
from .mocks import MockNasaApiClient, MockTwitterApiClient
from src.image_service import ImageService
from src.posting_service import PostingService
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
    image_service = ImageService(nasa_client)
    twitter_client = MockTwitterApiClient()
    posting_service = PostingService(twitter_client)
    storage = Storage(history_file)
    bot = Bot(image_service, posting_service, storage)
    return bot


def reset_history_file():
    data = [{"name": "Image Name", "date": "1111-11-11", "url": "www.example.com"}]
    with open(history_file, "w") as file:
        data_string = json.dumps(data)
        file.write(data_string)


def test_bot_can_post_an_image():
    bot = set_up_bot()
    image = bot.image_service.fetch_image()
    image_posted = bot.post_image(image)
    assert image_posted == True
    assert image.build_json() in bot.storage.data
    bot.posting_service.delete_tweet(bot.last_post_id)
    reset_history_file()
