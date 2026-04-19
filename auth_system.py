"""Authentication module for the Library Management System."""


DEFAULT_USERS = {
    "admin": {"password": "admin123", "role": "librarian"},
    "member": {"password": "member123", "role": "member"},
}



def authenticate(username: str, password: str, user_db: dict | None = None) -> bool:
    """Return True if the username and password match the user database."""
    user_db = user_db or DEFAULT_USERS
    user = user_db.get(username)
    return bool(user and user.get("password") == password)



def get_role(username: str, user_db: dict | None = None) -> str | None:
    """Return the role of an authenticated user."""
    user_db = user_db or DEFAULT_USERS
    user = user_db.get(username)
    return user.get("role") if user else None
