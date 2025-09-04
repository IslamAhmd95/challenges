import time
from .base_book import BaseBook

class EBook(BaseBook):
    def __init__(self, title, author, book_genre, price, published_at, location_to_save):
        super().__init__(title, author, book_genre, price, published_at)
        self.book_type = "ebook"
        self.location_to_save = location_to_save

    def save_book(self):
        print(f"Saving ({self.title}) book to ({self.location_to_save}) ...")
        self.simulate_action()
        print(f"Book ({self.title}) saved to this location ({self.location_to_save}).")

    def download_book(self):
        print(f"Downloading book ({self.title})")
        self.simulate_action()
        print(f"Book ({self.title}) downloaded.")

    @staticmethod
    def simulate_action():
        time.sleep(1)
