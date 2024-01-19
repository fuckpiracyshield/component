from piracyshield_component.validation.rule import Rule

import re

class FQDN(Rule):

    """
    Rule that checks for a valid fully qualified domain name.
    """

    message = 'FQDN not valid'

    expression = r'^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'

    def __init__(self):
        """
        Initialize parent __init__.
        """

        super().__init__()

    def __call__(self, value: any) -> None:
        """
        Checks for a valid FQDN.

        :param value: a valid string.
        """

        if not re.search(self.expression, value):
            self.register_error(self.message)
