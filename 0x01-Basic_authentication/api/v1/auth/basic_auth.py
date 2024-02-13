#!/usr/bin/env python3
""" Module of BasicAuth
"""

from .auth import Auth
import base64


class BasicAuth(Auth):
    """ "BasicAuth Class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extract_base64_authorization_header method"""
        if isinstance(authorization_header, str) and \
            authorization_header.startswith(
            "Basic "
        ):
            return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """decode_base64_authorization_header"""
        if isinstance(base64_authorization_header, str):
            try:
                decoded_bytes = base64.b64decode(base64_authorization_header)
                decoded_string = decoded_bytes.decode("utf-8")
                return decoded_string
            except (base64.binascii.Error, UnicodeDecodeError) as error:
                return None
