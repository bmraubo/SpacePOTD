from src.image_service import ImageService
from .mocks import MockNasaApiClient


def test_can_obtain_title_date_and_url():
    client = MockNasaApiClient()
    image_service = ImageService(client)
    image = image_service.get_data()
    assert image.name == "Partial Solar Eclipse over Argentina"
    assert image.date == "2022-05-02"
    assert (
        image.url
        == "https://apod.nasa.gov/apod/image/2205/PartialEclipse_Andrada_960.jpg"
    )

def test_image_service_obtains_image():
    api_client = MockNasaApiClient()
    image_service = ImageService(api_client)
    image = image_service.get_data()
    assert image.data != None
