from piracyshield_component.validation.rule import Rule

import re

class Email(Rule):

    """
    Rule that checks for a valid e-mail address.
    """

    message = 'The value must be a valid e-mail address'

    # support also second level domains
    expression = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]([a-z\-]+.)?\w+[.]\w{2,18}$'

    def __init__(self):
        """
        Initialize parent __init__.
        """

        super().__init__()

    def __call__(self, value: any) -> None:
        """
        Matches our regular expression against the given value.

        param: value: a valid string.
        """

        if not re.search(self.expression, value):
            self.register_error(self.message)
