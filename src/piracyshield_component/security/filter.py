import re

class Filter:

    """
    Generic input filter utility.
    """

    @staticmethod
    def strip(value: str, character: str = ' '):
        """
        Strips the character from the start and the end of a string.
        """

        return value.strip(character)

    @staticmethod
    def remove_whitespace(value: str):
        """
        Removes whitespaces from a string.
        """

        return re.sub(r'\s+', '', value)
