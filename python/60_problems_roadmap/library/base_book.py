import uuid
from datetime import date, datetime

from .abstract_book import AbstractBook
from .mixins import BookInfoMixin
from .descriptors import UpperCaseDescriptor, PositiveNumber


class BaseBook(AbstractBook, BookInfoMixin):

    title = UpperCaseDescriptor()
    author = UpperCaseDescriptor()
    price = PositiveNumber()

    def __init__(self, title: str, author: str, book_genre: str, price: float, published_at: date):
        self.__id = uuid.uuid4()
        self.title = title
        self.author = author
        self.book_genre = book_genre
        self.price = price
        self._published_at = published_at

    @property
    def id(self):
        return self.__id
    
    @property
    def published_at(self):
        # logic: format datetime to readable string
        if isinstance(self._published_at, datetime):
            return self._published_at.strftime("%B %d, %Y")  
        return str(self._published_at)

    def __repr__(self):
        return f"<Book id={self.id} title={self.title!r} author={self.author!r} price={self.price}>"
