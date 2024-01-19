from __future__ import annotations

import uuid
import secrets

class Identifier:

    """
    Class for identifiers generation.
    """

    def generate(self) -> str:
        """
        Generates RFC 4122 compliant ids.

        :return: a string based on the UUIDv4, minus the dashes.
        """

        string = uuid.uuid4()

        # converts to string and removes dashes producing a 32 characters value
        return string.hex

    def generate_short_unsafe(self, length: int = 8) -> str:
        """
        Generates a short handy string to be used in situations where we need to add a prefix or something like that.
        Does not guarantees the uniqueness, but that's not an issue for this kind of identifier usage.

        :param length: custom length of the string.
        :return: an alphanumeric string.
        """

        return secrets.token_hex(length)
