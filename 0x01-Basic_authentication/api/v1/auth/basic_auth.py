#!/usr/bin/env python3
""" Module of BasicAuth
"""
from .auth import Auth


class BasicAuth(Auth):
    """ "BasicAuth Class"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """extract_base64_authorization_header method"""
        if isinstance(authorization_header, str) and \
            authorization_header.startswith("Basic "):
            return authorization_header[len("Basic ") :]
