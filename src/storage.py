import typing
import json
from src.image import Image

class Storage:

    def __init__(self, history_file):
        self.history_file = history_file
        self.data = self.open_history_file()

    def open_history_file(self):
        with open(self.history_file, "r") as file:
            return json.loads(file.read())

    def write_to_history_file(self):
        pass
    
    def get_last_image(self) -> Image:
        return Image(self.data[-1])

    def add_image(self, image: Image):
        pass