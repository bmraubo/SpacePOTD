from src.twitter_connect import TwitterConnect
from io import BytesIO
import requests

def test_can_delete_tweets():
    test_tweet = "Gonna Delete This"
    twitter_connect = TwitterConnect()
    response_data = twitter_connect.post_text(test_tweet)
    delete_response = twitter_connect.delete_tweet(response_data["id"])
    print(delete_response)
    assert delete_response._json["id"] == response_data["id"]

def test_can_post_to_twitter():
    test_tweet = "Gonna Post Something"
    twitter_connect = TwitterConnect()
    response_data = twitter_connect.post_text(test_tweet)
    assert response_data["text"] == test_tweet
    twitter_connect.delete_tweet(response_data["id"])

def test_can_upload_media():
    file_name = "Partial Solar Eclipse over Argentina"
    fetched_file = requests.get("https://apod.nasa.gov/apod/image/2205/PartialEclipse_Andrada_960.jpg")
    file = BytesIO(fetched_file.content)
    twitter_connect = TwitterConnect()
    media_upload_response = twitter_connect.upload_media(file_name, file)
    print(media_upload_response)
    assert media_upload_response.media_id is not None

