from datetime import date
from library.base_book import BaseBook
from library.physical_book import PhysicalBook
from library.ebook import EBook
from library.library import Library
from library.member import Member

# 1. Create some books
book1 = PhysicalBook(
    title="Python 101",
    author="John Doe",
    book_genre="Programming",
    price=50,
    published_at=date(2022, 5, 15),
    shelf_location="A-12"
)

book2 = EBook(
    title="Clean Code",
    author="Robert Martin",
    book_genre="Software Engineering",
    price=40,
    published_at=date(2019, 8, 1),
    location_to_save="/ebooks/clean_code.pdf"
)

book3 = PhysicalBook(
    title="Data Science Handbook",
    author="Jane Smith",
    book_genre="Data",
    price=70,
    published_at=date(2021, 2, 20),
    shelf_location="B-07"
)

# 2. Create a library with books
library = Library(
    name="Central Library",
    location="Downtown",
    books=[book1, book2],
    owner="Mr. Librarian",
    rent=5000
)

print(library)  # repr


# 3. Create members 
member1 = Member("Alice", 25, library)
member2 = Member("Bob", 30, library)

print("Members:", library.members)


# 4. Add a new book later
library.add_books(book3)
print("Books in library after adding:", len(library))


# 5. Search books
print("Search 'python':", library.search_books("python"))
print("Search 'martin':", library.search_books("martin"))


# 6. Borrow and return books
library.borrow_book(member1, book1)
print("Borrowed books:", library.get_borrowed_books())


# Trying to borrow same book again → raises ValueError
try:
    library.borrow_book(member2, book1)
except ValueError as e:
    print("Error:", e)

# Returning book
library.return_book(member1)
print("Borrowed books after return:", library.get_borrowed_books())


# 7. EBook actions
book2.download_book()
book2.save_book()


# 8. Display book info (mixin)
print(book1.display_book_info())
print(book2.display_book_info())
