#!/usr/bin/env python3

"""
This module provides a simple authentication mechanism for the application.
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Returns a salted hash of the input password."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
