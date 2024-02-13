#!/usr/bin/env python3
""" Module of auth
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ "Auth Class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth
        arg:
            @path
            @excluded_paths
        return True if path not in excluded_paths
        """
        if bool(path and excluded_paths):
            path = path + "/" if path[-1] != "/" else path
            return path not in excluded_paths
        return True

    def authorization_header(self, request=None) -> str:
        """authorization header method
        return None
        """
        return None

    def current_user(self, request=None) -> TypeVar("User"):  # type: ignore
        """get current user
        return None
        """
        return None
