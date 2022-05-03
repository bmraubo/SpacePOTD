from src.twitter_connect import TwitterConnect

def test_can_delete_tweets():
    test_tweet = "Gonna Delete This"
    twitter_connect = TwitterConnect()
    response_data = twitter_connect.post_text(test_tweet)
    delete_response = twitter_connect.delete_tweet(response_data["id"])
    print(delete_response)
    assert delete_response._json["id_str"] == str(response_data["id"])

def test_can_post_to_twitter():
    test_tweet = "Gonna Post Something"
    twitter_connect = TwitterConnect()
    response_data = twitter_connect.post_text(test_tweet)
    assert response_data["text"] == test_tweet
    twitter_connect.delete_tweet(response_data["id"])