from piracyshield_component.validation.rule import Rule

import re

class ASCode(Rule):

    """
    Rule that checks for a valid AS code.
    """

    message = 'AS code not valid'

    expression = r'^(AS)?[0-9]{1,10}$'

    def __init__(self):
        """
        Initialize parent __init__.
        """

        super().__init__()

    def __call__(self, value: str) -> None:
        """
        Checks the validity of the AS code.
        It's flexible enough to allow also non AS/A prefix strings.

        :param value: a valid string.
        """

        if not re.search(self.expression, value):
            self.register_error(self.message)
