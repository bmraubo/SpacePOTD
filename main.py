from src.posting_service import TwitterApiClient, PostingService
from src.image_service import ImageService, NasaApiClient
from src.storage import Storage
from src.settings import HISTORY_FILE, LOG_FILE
from src.bot import Bot
import logging

def start_logging(log_file):
    logging.basicConfig(filename=log_file, filemode="a", format="%(asctime)s %(levelname)s: %(message)s", level=logging.DEBUG)
    logging.info("Logging...")

def main():
    start_logging(LOG_FILE)
    nasa_api_client = NasaApiClient()
    nasa_connect = ImageService(nasa_api_client)
    twitter_api_client = TwitterApiClient()
    twitter_connect = PostingService(twitter_api_client)
    storage = Storage(HISTORY_FILE)
    bot = Bot(nasa_connect, twitter_connect, storage)
    bot.start()

if __name__ == "__main__":
    main()
