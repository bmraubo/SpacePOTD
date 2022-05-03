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
        auth = tweepy.OAuth1UserHandler(self.consumer_key,self.consumer_secret,self.access_token, self.access_token_secret)
        client = tweepy.API(auth)
        return client

    def post_text(self, text):
        response = self.client.update_status(status=text)
        return response._json

    def post_text_with_image(self, text, image_path):
        self.client.create_tweet()

    def delete_tweet(self, tweet_id):
        return self.client.destroy_status(tweet_id)
