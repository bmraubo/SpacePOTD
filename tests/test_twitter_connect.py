from src.twitter_connect import TwitterConnect
from io import BytesIO
import requests

def test_can_delete_tweets():
    test_tweet = "Gonna Delete This"
    twitter_connect = TwitterConnect()
    response_data = twitter_connect.post_text(test_tweet)
    delete_response = twitter_connect.delete_tweet(response_data._json["id"])
    print(delete_response)
    assert delete_response._json["id"] == response_data._json["id"]

def test_can_post_to_twitter():
    test_tweet = "Gonna Post Something"
    twitter_connect = TwitterConnect()
    response_data = twitter_connect.post_text(test_tweet)
    assert response_data._json["text"] == test_tweet
    twitter_connect.delete_tweet(response_data._json["id"])

def test_can_upload_media():
    file_name = "Partial Solar Eclipse over Argentina"
    fetched_file = requests.get("https://apod.nasa.gov/apod/image/2205/PartialEclipse_Andrada_960.jpg")
    file = BytesIO(fetched_file.content)
    twitter_connect = TwitterConnect()

    media_upload_response = twitter_connect.upload_media(file_name, file)

    assert type(media_upload_response.media_id) is int

def test_can_post_to_twitter_with_media():
    text = "Posting a Picture!"
    file_name = "Partial Solar Eclipse over Argentina"
    fetched_file = requests.get("https://apod.nasa.gov/apod/image/2205/PartialEclipse_Andrada_960.jpg")
    file = BytesIO(fetched_file.content)
    twitter_connect = TwitterConnect()
    media_upload_response = twitter_connect.upload_media(file_name, file)
    media_id = media_upload_response.media_id

    post_response = twitter_connect.post_text_with_image(text, media_id)
    media_information = post_response._json["entities"]["media"][0]

    assert media_id == media_information["id"]
    assert text in post_response._json["text"]
    twitter_connect.delete_tweet(post_response._json["id"])

