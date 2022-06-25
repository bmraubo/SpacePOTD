import tweepy
import logging
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

    def update_status():
        pass

    def media_upload():
        pass
    
    def destroy_status():
        pass

class TwitterConnect:

    def __init__(self, client):
        self.client = client

    def create_client(self):
        auth = tweepy.OAuth1UserHandler(
            self.consumer_key,
            self.consumer_secret,
            self.access_token,
            self.access_token_secret,
        )
        client = tweepy.API(auth)
        return client

    def post_text(self, text):
        logging.info("posting update with text")
        return self.client.update_status(status=text)

    def post_text_with_image(self, text, media_id):
        logging.info("posting update with text and image")
        return self.client.update_status(status=text, media_ids=[str(media_id)])

    def upload_media(self, file_name, file):
        logging.info("uploading media")
        return self.client.media_upload(filename=file_name, file=file)

    def delete_tweet(self, tweet_id):
        return self.client.destroy_status(tweet_id)
