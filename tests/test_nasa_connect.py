from src.nasa_connect import NasaConnect
from .mocks import MockNasaApiClient

def test_can_obtain_title_and_url():
    api_client = MockNasaApiClient()
    nasa_connect = NasaConnect(api_client)
    nasa_connect_data = nasa_connect.get_data()
    assert nasa_connect_data["title"] == "Partial Solar Eclipse over Argentina"
    assert nasa_connect_data["url"] == "https://apod.nasa.gov/apod/image/2205/PartialEclipse_Andrada_960.jpg"

