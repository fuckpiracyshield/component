from __future__ import annotations

import argon2

class Hasher:

    """
    Helper class to encode and verify strings. Used as password encoder.
    """

    hasher_instance = None

    def __init__(self, time_cost: int, memory_cost: int, parallelism: int, hash_length: int, salt_length: int):
        """
        Initialize the instance and sets the options.

        !! THESE PARAMETERS SHOULD NOT BE CHANGED AFTER THE FIRST USAGE !!

        :param time_cost: execution time cost of the hashing operation.
        :param memory_cost: memory usage of the hasing operation.
        :param parallelism: quantity of parallel threads used.
        :param hash_length: length of the hash.
        :param salt_length: length of the generated salt.
        """

        self.hasher_instance = argon2.PasswordHasher(
            time_cost = time_cost,
            memory_cost = memory_cost,
            parallelism = parallelism,
            hash_len = hash_length,
            salt_len = salt_length,
            type = argon2.low_level.Type.ID
        )

    def encode_string(self, string: str) -> str:
        """
        Encode the string as an argon2 hash.

        :param str: the string to hash.
        :return: the encoded argon2 hash.
        """

        try:
            # generate the hash
            hashed_string = self.hasher_instance.hash(string)

        except argon2.exceptions.HashingError:
            raise HasherGenericException()

        return hashed_string

    def verify_hash(self, string: str, hashed_string: str) -> bool | Exception:
        """
        Verify the string against the hash.

        :param string: the string to verify.
        :param hashed_string: the argon2 hash to verify against.
        :return: True if the plaintext password matches the hash, otherwise False.
        """

        try:
            return self.hasher_instance.verify(hashed_string, string)

        except argon2.exceptions.VerificationError:
            raise HasherNonValidException()


class HasherGenericException(Exception):

    """
    Raised during the encoding of the plain text string.
    """

class HasherNonValidException(Exception):

    """
    Raised during the verification procedure, if the string is not matching the hash.
    """
