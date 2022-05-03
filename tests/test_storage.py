from src.image import Image
from src.storage import Storage

def set_up_image():
    data = {
        "name": "Partial Solar Eclipse over Argentina",
        "date": "2022-05-02",
        "url": "https://apod.nasa.gov/apod/image/2205/PartialEclipse_Andrada_960.jpg" 
    }
    image = Image(data)
    return image


def test_can_open_history_file():
    history_file = "tests/test_history.txt"
    storage = Storage(history_file)
    assert type(storage.data) == list

def test_can_get_last_image_data():
    history_file = "tests/test_history.txt"
    storage = Storage(history_file)
    last_image = storage.get_last_image()
    assert last_image.name == "Image Name"
    assert last_image.date == "1111-11-11"
    assert last_image.url == "www.example.com"

def test_can_write_to_history_file():
    history_file = "tests/test_history.txt"
    image = set_up_image()
    storage = Storage(history_file)
    storage.add_image(image)
    last_image = storage.get_last_image()
    assert last_image.name == "Partial Solar Eclipse over Argentina"
    assert last_image.date == "2022-05-02"
    assert last_image.name == "https://apod.nasa.gov/apod/image/2205/PartialEclipse_Andrada_960.jpg" 
