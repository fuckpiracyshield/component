from piracyshield_component.validation.rule import Rule

class IPv6(Rule):

    """
    Rule that checks for a valid IPv6.
    """

    hextets_syntax_message = 'IPv6 not valid, more than one `::` found'

    hextets_message = 'IPv6 not valid, expecting eight hextets, got {}'

    hextets_digits_message = 'IPv6 not valid, expecting eight hextets of hexadecimal digits'

    hextets_maximum_length = 'IPv6 not valid, too many hextets'

    hextets_length_message = 'IPv6 not valid, one or more hextet(s) too long'

    hextets_digits_size_message = 'IPv6 not valid, expecting hexadecimal digits from 0 to FFFF'

    def __init__(self):
        """
        Initialize parent __init__.
        """
        super().__init__()

    def __call__(self, value: str) -> None:
        """
        Checks the validity of the passed string.
        Instead of relying on regular expression, it's better to check the individual hextets.
        This also allows for better error reporting.

        :param value: a valid string.
        """

        # short syntax
        if '::' in value:
            parts = value.split('::')

            if len(parts) > 2:
                self.register_error(self.hextets_syntax_message)

                return False

            left_side = parts[0].split(':') if parts[0] else []
            right_side = parts[1].split(':') if parts[1] else []

            zeros_needed = 8 - len(left_side) - len(right_side)

            if zeros_needed < 0:
                self.register_error(self.hextets_maximum_length)

                return False

            hextets = left_side + ['0'] * zeros_needed + right_side

        # common syntax
        else:
            hextets = value.split(':')

            if len(hextets) != 8:
                self.register_error(self.hextets_message.format(self.hextets_digits_message))

                return False

        for hextet in hextets:
            if not all(c in '0123456789ABCDEFabcdef' for c in hextet):
                self.register_error(self.hextets_digits_message)

                return False

            if len(hextet) > 4:
                self.register_error(self.hextets_length_message)

                return False

            try:
                int_value = int(hextet, 16)

                if not (0 <= int_value <= 0xFFFF):
                    self.register_error(self.hextets_digits_size_message)

                    return False

            except ValueError:
                self.register_error(self.hextets_digits_size_message)

                return False
