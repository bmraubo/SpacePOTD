import typing
import logging
import json
from os.path import exists
from src.image import Image


class Storage:
    def __init__(self, history_file):
        logging.info("Initializing Storage")
        self.history_file = history_file
        self.data = self.load_history()

    def open_history_file(self):
        logging.info("Opening History File")
        with open(self.history_file, "r") as file:
            return json.loads(file.read())

    def write_to_history_file(self):
        with open(self.history_file, "w") as file:
            data_string = json.dumps(self.data)
            file.write(data_string)
            logging.info("History File Updated")

    def get_last_image(self) -> Image:
        return Image(self.data[-1])

    def add_image(self, image: Image):
        logging.info(f"Adding Image (Date: {image.date}) to History")
        self.data.append(image.build_json())
        self.write_to_history_file()

    def file_exists(self):
        return exists(self.history_file)

    def generate_new_history_file(self):
        logging.info("Creating New History File")
        self.data = []
        self.write_to_history_file()

    def load_history(self):
        if self.file_exists():
            logging.info("History File Found")
            return self.open_history_file()
        else:
            logging.info("History File Not Found")
            self.generate_new_history_file()
            return self.open_history_file()
