from src.twitter_connect import TwitterConnect
from src.nasa_connect import NasaConnect, NasaApiClient
from src.bot import Bot

if __name__ == "__main__":
    nasa_api_client = NasaApiClient()
    nasa_connect = NasaConnect(nasa_api_client)
    twitter_connect = TwitterConnect()
    bot = Bot(nasa_connect, twitter_connect)
    bot.start()
