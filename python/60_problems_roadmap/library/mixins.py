class BookInfoMixin:
    """
    Provides a method to display book details.

    Requires:
        self.title
        self.author
        self.published_at
    """
    def display_book_info(self) -> str:
        return f"The book named {self.title} is authored by {self.author} and published at {self.published_at}"