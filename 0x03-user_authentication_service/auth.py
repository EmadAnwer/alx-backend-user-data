#!/usr/bin/env python3

"""
This module provides a simple authentication mechanism for the application.
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Returns a salted hash of the input password."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        """Constructor method"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a user in the database."""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {email} already exists")

        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))