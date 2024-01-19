import datetime
import time

import pytz

class Time:

    """
    Handy utility for date and/or time generation.
    """

    TIMEZONE = 'Europe/Rome'

    @staticmethod
    def now() -> str:
        """
        Returns the current date and time.

        :return: the current date and time as a string.
        """

        timezone = pytz.timezone(Time.TIMEZONE)

        utc = datetime.datetime.now()

        return utc.astimezone(timezone)

    def now_format(datetime_format: str) -> str:
        """
        Returns the current date and time using a custom format.

        :return: the current date and time as a string.
        """

        now = Time.now()

        return now.strftime(datetime_format)

    @staticmethod
    def now_iso8601() -> str:
        """
        Returns the current date and time in ISO 8601 format.

        :return: the current date and time as a string.
        """

        now = Time.now()

        return now.isoformat()

    @staticmethod
    def timestamp():
        """
        Returns the current Unix timestamp as an integer.

        :return: the current Unix timestamp.
        """

        now = Time.now()

        return int(now.timestamp())

    @staticmethod
    def timestamp_to_datetime(timestamp: int) -> bool | Exception:
        try:
            # convert the timestamp to a datetime with timezone information
            return datetime.datetime.fromtimestamp(timestamp, tz = pytz.timezone(Time.TIMEZONE))

        except ValueError:
            raise TimeValueException()

    @staticmethod
    def is_expired(date: int, expiration_time: int) -> bool:
        """
        Checks if the provided date is expired.

        :param date: a date in ISO8601 format.
        :param expiration_time: the distance in seconds for the date to expiry.
        :return: true if expired.
        """

        # convert the date string to a datetime object
        datetime_object = datetime.datetime.fromisoformat(date)

        # sum the expired time to the date
        converted_date = datetime_object + datetime.timedelta(seconds = expiration_time)

        current_date = Time.now()

        return current_date > converted_date

    def is_valid_iso8601(date: int) -> bool | Exception:
        """
        Validates the date against the ISO8601 format.

        :param date: a date in ISO8601 format.
        :return: true if the date format is correct.
        """

        try:
            datetime.datetime.fromisoformat(date)

            return True

        except:
            raise TimeFormatException()

class TimeValueException(Exception):

    """
    Wrong input.
    """

    pass

class TimeFormatException(Exception):

    """
    Wrong date format.
    """

    pass
