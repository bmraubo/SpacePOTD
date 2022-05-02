import pytest
from src.nasa_connect import NasaConnect

def test_can_connect_to_nasa_api():
    response = NasaConnect().get_data()
    assert response.status_code == 200