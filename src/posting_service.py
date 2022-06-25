import logging

class PostingService:

    def __init__(self, client):
        self.client = client

    def post_text(self, text):
        logging.info("posting update with text")
        return self.client.update_status(status=text)

    def post_text_with_image(self, text, media_id):
        logging.info("posting update with text and image")
        return self.client.update_status(status=text, media_ids=[str(media_id)])

    def upload_media(self, file_name, file):
        logging.info("uploading media")
        return self.client.upload_media(filename=file_name, file=file)

    def delete_tweet(self, tweet_id):
        return self.client.delete_tweet(tweet_id)
