"""Library module for the Library Management System."""

from book import Book
from member import Member


class Library:
    """Manages books and members in the library."""

    def __init__(self) -> None:
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}

    def add_book(self, book: Book) -> None:
        """Add a book to the library or increase copies if it already exists."""
        if book.isbn in self.books:
            self.books[book.isbn].add_copies(book.copies)
        else:
            self.books[book.isbn] = book

    def remove_book(self, isbn: str) -> None:
        """Remove a book completely from the library catalog."""
        if isbn not in self.books:
            raise KeyError("book not found")
        del self.books[isbn]

    def get_book(self, isbn: str) -> Book | None:
        """Return a book by ISBN, or None if it is not found."""
        return self.books.get(isbn)

    def list_books(self) -> list[Book]:
        """Return all books in the library as a list."""
        return list(self.books.values())

    def register_member(self, member: Member) -> None:
        """Register a new library member."""
        if member.member_id in self.members:
            raise ValueError("member already exists")
        self.members[member.member_id] = member

    def get_member(self, member_id: str) -> Member | None:
        """Return a member by ID, or None if not found."""
        return self.members.get(member_id)

    def list_members(self) -> list[Member]:
        """Return all registered members."""
        return list(self.members.values())
