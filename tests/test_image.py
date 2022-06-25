from src.image import Image

MOCK_NASA_API_DATA = {
    "name": "Partial Solar Eclipse over Argentina",
    "date": "2022-05-02",
    "url": "https://apod.nasa.gov/apod/image/2205/PartialEclipse_Andrada_960.jpg",
}


def test_image_is_constructed():
    image = Image(MOCK_NASA_API_DATA)

    assert image.name == "Partial Solar Eclipse over Argentina"
    assert image.date == "2022-05-02"
    assert (
        image.url
        == "https://apod.nasa.gov/apod/image/2205/PartialEclipse_Andrada_960.jpg"
    )


def test_can_fetch_image():
    image = Image(MOCK_NASA_API_DATA)
    image.fetch_image()
    assert image.data != None
    assert image.ready == True


def test_has_been_posted():
    last_posted_image_date = "2022-05-02"
    image = Image(MOCK_NASA_API_DATA)
    posted = image.has_been_posted(last_posted_image_date)
    assert posted == True
