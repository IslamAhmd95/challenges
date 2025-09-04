from __future__ import annotations  # ✅ enables using "Member" as a string type hint

from .base_book import BaseBook
from .descriptors import UpperCaseDescriptor
# from .member import Member  


class Library:

    name = UpperCaseDescriptor()

    def __init__(self, name: str, location: str, books: list[BaseBook], owner: str, rent: int):
        self.name = name
        self.location = location
        self.books = self.__validating_books(books)
        self.owner = owner
        self.__rent = rent
        self._members = []
        self._borrowed_books = dict()

    @property
    def rent(self):
        return self.__rent
    
    @rent.setter
    def rent(self, new_rent):
        if new_rent < 0:
            raise ValueError("Rent can't be less than 0")
        self.__rent = new_rent

    @property
    def members(self):
        return self._members
    
    def add_member(self, member: "Member"):

        from .member import Member   # ✅ lazy import to avoid circular issues
        
        if not isinstance(member, Member):
            raise ValueError("Member must be an instance of Member class.")
        if member not in self._members:
            self._members.append(member)
    

    def get_borrowed_books(self):
        return self._borrowed_books
    
    def set_borrowed_books(self, member: "Member", book: BaseBook):

        from .member import Member   # ✅ lazy import to avoid circular issues

        if not isinstance(member, Member):
            raise ValueError("Member must be an instance of Member class.")
        if not isinstance(book, BaseBook):
            raise ValueError("Book must be an instance of BaseBook class.")
        if book not in self.books:
            raise ValueError("This book does not exist in the library.")
        if book in self._borrowed_books.values():
            raise ValueError("This book is already borrowed.")
        if member in self._borrowed_books: 
            raise ValueError("This member already borrowed a book.")
        self._borrowed_books[member] = book


    def __len__(self):
        return len(self.books)

    def __iter__(self):
        return iter(self.books)

    def __contains__(self, book: BaseBook):
        return book in self.books

    def __repr__(self):
        return f"<Library name={self.name!r}, books={len(self)}, location={self.location!r}>"

    def add_books(self, book: BaseBook):
        if not isinstance(book, BaseBook):
            raise TypeError("Book must be an instance of BaseBook or its subclasses.")
        if book in self.books:
            raise ValueError("This book already exists in the library.")
        self.books.append(book)
    
    def search_books(self, query):
        if not query:
            raise ValueError("Enter the book title or the author name")
        
        query = query.lower()
        results = [
            book for book in self.books if query in book.title.lower() or query in book.author.lower()
        ]
        return results or None
    
    @staticmethod
    def __validating_books(books):
        if not isinstance(books, list):
            raise TypeError("Books must be provided as a list.")
        if not books:
            raise ValueError("Library must be initialized with at least one book.")
        if not all(isinstance(book, BaseBook) for book in books):
            raise TypeError("All items in books must be instances of BaseBook or its subclasses.")
        return books
    
    def borrow_book(self, member: "Member", book: BaseBook):
        self.set_borrowed_books(member, book)

    def return_book(self, member: "Member"):
        if member not in self._borrowed_books:
            raise ValueError("This member has not borrowed any book.")
        del self._borrowed_books[member]


"""
Notes:

    1. Circular import risk

        - The issue

            library.py imports Member

            member.py imports Library

        This is called a circular import.

        What happens?

            When Python loads library.py, it sees:
                from .member import Member
            So it tries to load member.py.
            But member.py also says:
                from .library import Library
            So Python tries to load library.py again while it’s not fully ready.
            This leads to ImportError: cannot import name 'X' from partially initialized module.

            It might not always break (depends on import order), but it’s risky.
        
        The fix

            We don’t actually need to import Member inside library.py, because Member is only used for type hints.
                from __future__ import annotations  # ✅ enables using "Member" as a string type hint

""" 