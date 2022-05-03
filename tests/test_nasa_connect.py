from src.nasa_connect import NasaConnect
from src.twitter_connect import TwitterConnect

class MockNasaApiClient:

    def get_data(self):
        return {
	        "copyright": "Aixa Andrada",
            "date": "2022-05-02",
            "explanation": "What's happened to the Sun? Two days ago, parts of South America were treated to a partial solar eclipse -- where the Moon blocked out part of the Sun.  The featured image shows an image of the partially eclipsed Sun through clouds as it was setting over Patagonia, Argentina. In the tilted image, Earth is toward the right. During the eclipse, the Moon moved partly between Earth and the Sun. Although a visually impressive sight, the slight dimming of surroundings  during this partial eclipse was less noticeable than dimming created by a thick cloud. In about two weeks, all of South America and part of North America will experience a total lunar eclipse -- where the Earth moves completely between the Moon and the Sun.  In about two years, a total solar eclipse will cross North America.",
            "hdurl": "https://apod.nasa.gov/apod/image/2205/PartialEclipse_Andrada_2048.jpg",
            "media_type": "image",
            "service_version": "v1",
            "title": "Partial Solar Eclipse over Argentina",
            "url": "https://apod.nasa.gov/apod/image/2205/PartialEclipse_Andrada_960.jpg"
        }

def test_can_obtain_title_and_url():
    api_client = MockNasaApiClient()
    nasa_connect = NasaConnect(api_client)
    nasa_connect_data = nasa_connect.get_data()
    assert nasa_connect_data["title"] == "Partial Solar Eclipse over Argentina"
    assert nasa_connect_data["url"] == "https://apod.nasa.gov/apod/image/2205/PartialEclipse_Andrada_960.jpg"

