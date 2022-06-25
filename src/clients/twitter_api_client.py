import tweepy
from src.settings import (
    TWITTER_BEARER_TOKEN,
    TWITTER_CONSUMER_KEY,
    TWITTER_CONSUMER_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_SECRET,
)

class TwitterApiClient:
    consumer_key = TWITTER_CONSUMER_KEY
    consumer_secret = TWITTER_CONSUMER_SECRET
    access_token = TWITTER_ACCESS_TOKEN
    access_token_secret = TWITTER_ACCESS_SECRET
    bearer_token = TWITTER_BEARER_TOKEN

    def __init__(self):
        self.client = self.create_client()

    def create_client(self):
        auth = tweepy.OAuth1UserHandler(
            self.consumer_key,
            self.consumer_secret,
            self.access_token,
            self.access_token_secret,
        )
        client = tweepy.API(auth)
        return client

    def update_status(self, status, media_ids=None):
        if media_ids != None:
            return self.client.update_status(status=status, media_ids=media_ids)
        return self.client.update_status(status=status)

    def upload_media(self, filename, file):
        return self.client.media_upload(filename=filename, file=file)
    
    def destroy_status(self, tweet_id):
        return self.client.destroy_status(tweet_id)
