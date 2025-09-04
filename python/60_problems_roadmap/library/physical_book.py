from .base_book import BaseBook

class PhysicalBook(BaseBook):
    def __init__(self, title, author, book_genre, price, published_at, shelf_location):
        super().__init__(title, author, book_genre, price, published_at)
        self.book_type = "physical"
        self.shelf_location = shelf_location
