from piracyshield_component.validation.rule import Rule

import re

class DDA(Rule):

    """
    Rule that checks for a valid DDA identifier.
    """

    message = 'DDA identifier not valid'

    expression = r'^[0-9]{1,4}\/[0-9]{2}\/DDA$'

    def __init__(self):
        """
        Initialize parent __init__.
        """

        super().__init__()

    def __call__(self, value: str) -> None:
        """
        Checks the validity of the DDA identifier.

        :param value: a valid string.
        """

        if not re.search(self.expression, value):
            self.register_error(self.message)
