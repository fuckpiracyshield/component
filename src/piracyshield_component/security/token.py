from __future__ import annotations

from piracyshield_component.utils.time import Time, TimeValueException

import jwt
import datetime

class JWTToken:

    """
    Class for the management of the JWT token.
    """

    secret_key = None

    algorithm = None

    expiration_time = None

    def __init__(self, access_secret_key: str, refresh_secret_key: str, access_expiration_time: int, refresh_expiration_time: int, algorithm: str):
        """
        Sets the options.

        !! THESE PARAMETERS SHOULD NOT BE CHANGED AFTER THE FIRST USAGE !!

        :param access_secret_key: the secret key for the access token generation.
        :param access_secret_key: the secret key for the refresh token generation.
        :param access_expiration_time: time duration for the access token, set in seconds.
        :param access_expiration_time: time duration for the refresh token, set in seconds.
        :param algorithm: algorithm for encoding and decoding (default: HS256).
        """

        self.access_secret_key = access_secret_key

        self.refresh_secret_key = refresh_secret_key

        self.access_expiration_time = access_expiration_time

        self.refresh_expiration_time = refresh_expiration_time

        self.algorithm = algorithm

    def generate_access_token(self, payload: dict) -> str | Exception:
        """
        Handles the generation of an access token using the configuration data.
        It's a short lived token that needs to be refreshed periodically.

        :param payload: dictionary containing the data to encode.
        :return: a JWT token signed with the secret key and encoded in base64.
        """

        return self.generate_token(payload, self.access_secret_key, self.access_expiration_time)

    def generate_refresh_token(self, payload: dict) -> str | Exception:
        """
        Handles the generation of a refresh token using the configuration data.
        This is intended as a long lived token, used to periodically refresh the access token.

        :param payload: dictionary containing the data to encode.
        :return: a JWT token signed with the secret key and encoded in base64.
        """

        return self.generate_token(payload, self.refresh_secret_key, self.refresh_expiration_time)

    def generate_token(self, payload: dict, secret_key: str, period: int) -> str | Exception:
        """
        Generate a JWT token with the given payload.

        :param payload: a dictionary containing the data to be encoded in the JWT token.
        :return: a JWT token signed with the secret key and encoded in base64.
        """

        # calculate the expiration time
        now = Time.now()

        # add the issued time
        payload['iat'] = now

        # add the expiration time
        payload['exp'] = now + datetime.timedelta(seconds = period)

        try:
            # generate the final token
            token = jwt.encode(payload, secret_key, algorithm = self.algorithm)

            return token

        # TODO: get a more granular error reporting here
        except Exception as e:
            raise JWTTokenGenericException()

    def verify_access_token(self, token: any) -> dict | Exception:
        """
        Verifies the access token with the configured access secret key.

        :param token: a valid JWT access token.
        :return: the original payload.
        """

        return self.verify_token(token, self.access_secret_key)

    def verify_refresh_token(self, token: any) -> dict | Exception:
        """
        Verifies the refresh token with the configured refresh secret key.

        :param token: a valid JWT access token.
        :return: the original payload.
        """

        return self.verify_token(token, self.refresh_secret_key)

    def verify_token(self, token: any, secret_key: str) -> dict | Exception:
        """
        Verify the given JWT token and return the decoded payload if the token is valid.

        :param token: a JWT token encoded in base64.
        :return: the decoded payload if the token is valid, otherwise an exception will be raised.
        """

        try:
            payload = jwt.decode(token, secret_key, algorithms = [self.algorithm])

            # check if it's expired
            try:
                if Time.timestamp_to_datetime(payload['exp']) < Time.now():
                    raise JWTTokenExpiredException()

            except TimeValueException:
                raise JWTTokenNonValidException()

            return payload

        except jwt.exceptions.ExpiredSignatureError:
            raise JWTTokenExpiredException()

        # TODO: should deal with more explicit exceptions on our side
        except (
            jwt.exceptions.InvalidTokenError,
            jwt.exceptions.InvalidSignatureError,
            jwt.exceptions.DecodeError,
            jwt.exceptions.InvalidAlgorithmError
        ):
            raise JWTTokenNonValidException()

class JWTTokenGenericException(Exception):

    """
    Generic exception as a last option.
    """

    pass

class JWTTokenExpiredException(Exception):

    """
    Exception raised on token expired time.
    """

    pass

class JWTTokenNonValidException(Exception):

    """
    Raised during the token verification, if there's no valid match.
    """

    pass
