import tweepy
from src.settings import (
    TWITTER_CONSUMER_KEY,
    TWITTER_CONSUMER_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_SECRET,
)

class TwitterApiClient:

    def __init__(self):
        self.client = self.create_client()

    def create_client(self):
        auth = tweepy.OAuth1UserHandler(
            TWITTER_CONSUMER_KEY,
            TWITTER_CONSUMER_SECRET,
            TWITTER_ACCESS_TOKEN,
            TWITTER_ACCESS_SECRET,
        )
        client = tweepy.API(auth)
        return client

    def update_status(self, status, media_ids=None):
        if media_ids != None:
            return self.client.update_status(status=status, media_ids=media_ids)
        return self.client.update_status(status=status)

    def upload_media(self, filename, file):
        return self.client.media_upload(filename=filename, file=file)
    
    def delete_tweet(self, tweet_id):
        return self.client.destroy_status(tweet_id)
