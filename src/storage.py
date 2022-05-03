import typing
import json
from src.image import Image

class Storage:

    def __init__(self, history_file):
        self.history_file = history_file

    def open_history_file(self):
        with open(self.history_file, "r") as file:
            self.data = json.loads(file.read())
    
    def get_last_image(self) -> Image:
        pass

    def add(self, image: Image):
        pass