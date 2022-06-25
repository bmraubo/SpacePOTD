from src.clients.nasa_api_client import NasaAPIClient
from src.clients.twitter_api_client import TwitterApiClient
from src.image_service import ImageService
from src.posting_service import PostingService
from src.storage import Storage
from src.bot import Bot
from os.path import join
import json

history_file = join("tests", "mock_history.txt")

def set_up_bot():
    nasa_client = NasaAPIClient()
    image_service = ImageService(nasa_client)
    twitter_client = TwitterApiClient()
    posting_service = PostingService(twitter_client)
    storage = Storage(history_file)
    bot = Bot(image_service, posting_service, storage)
    return bot

def reset_history_file():
    data = [{"name": "Image Name", "date": "1111-11-11", "url": "www.example.com"}]
    with open(history_file, "w") as file:
        data_string = json.dumps(data)
        file.write(data_string)

def test_bot_fetching_and_posting_an_image():
    reset_history_file()
    bot = set_up_bot()
    bot.update()
    assert bot.last_update_successful == True
    bot.posting_service.delete_tweet(bot.last_post_id)
    reset_history_file()