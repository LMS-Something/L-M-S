"""Issue and return functionality for the Library Management System."""

from library import Library


def issue_book(library: Library, isbn: str, member_id: str) -> str:
    """Issue a book to a member if a copy is available."""
    book = library.get_book(isbn)
    member = library.get_member(member_id)

    if book is None:
        return "Book not found."
    if member is None:
        return "Member not found."
    if not book.is_available():
        return "No copies available."

    book.remove_copy()
    member.borrow_book(isbn)
    return f"Book '{book.title}' issued to {member.name}."



def return_book(library: Library, isbn: str, member_id: str) -> str:
    """Return a book from a member to the library."""
    book = library.get_book(isbn)
    member = library.get_member(member_id)

    if book is None:
        return "Book not found."
    if member is None:
        return "Member not found."
    if isbn not in member.borrowed_books:
        return "This member did not borrow that book."

    member.return_book(isbn)
    book.add_copies(1)
    return f"Book '{book.title}' returned by {member.name}."
