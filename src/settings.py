from dotenv import load_dotenv
from os import getenv, path

load_dotenv()

HISTORY_FILE = path.join("data", "history.txt")
LOG_FILE = path.join("data", "spacepotd.log")

# API KEYS
NASA_API_KEY = getenv("NASA_API_KEY")
TWITTER_CONSUMER_KEY = getenv("TWITTER_CONSUMER_KEY")
TWITTER_CONSUMER_SECRET = getenv("TWITTER_CONSUMER_SECRET")
TWITTER_ACCESS_TOKEN = getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = getenv("TWITTER_ACCESS_SECRET")
TWITTER_BEARER_TOKEN = getenv("TWITTER_BEARER_TOKEN")
