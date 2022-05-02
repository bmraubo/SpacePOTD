import tweepy
from .settings import TWITTER_BEARER_TOKEN, TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET

class TwitterConnect:
    consumer_key = TWITTER_CONSUMER_KEY 
    consumer_secret = TWITTER_CONSUMER_SECRET
    access_token = TWITTER_ACCESS_TOKEN
    access_token_secret = TWITTER_ACCESS_SECRET
    bearer_token = TWITTER_BEARER_TOKEN

    def __init__(self):
        self.client = self.create_client()

    def create_client(self):
        client = tweepy.Client(
            bearer_token=self.bearer_token,
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret,
            access_token=self.access_token,
            access_token_secret=self.access_token_secret
        )
        return client

    def post_text(self, text):
        response = self.client.create_tweet(text=text)
        return response.data

    def post_text_with_image(self, text, image_path):
        pass

    def delete_tweet(self, tweet_id):
        return self.client.delete_tweet(tweet_id)
