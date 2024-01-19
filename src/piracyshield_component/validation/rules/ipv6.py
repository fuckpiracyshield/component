from piracyshield_component.validation.rule import Rule

class IPv6(Rule):

    """
    Rule that checks for a valid IPv6.
    """

    hextets_message = 'IPv6 not valid, expecting eight hextets, got {}'

    hextets_digits_message = 'IPv6 not valid, expecting eight hextets of hexadecimal digits'

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

        hextets = value.split(':')

        hextets_size = len(hextets)

        # we're expecting 8 hextets
        if hextets_size != 8:
            self.register_error(self.hextets_message.format(hextets_size))

        for hextet in hextets:
            single_hextet_size = len(hextet)

            # each hextet must be composed of hexadecimal digits
            if not all(c in '0123456789ABCDEFabcdef' for c in hextet):
                self.register_error(self.hextets_digits_message)

            # with a maximum length of 4
            if single_hextet_size > 4:
                self.register_error(self.hextets_length_message)

            try:
                # convert the hextet to an integer in base 16
                int_value = int(hextet, 16)

                # check if the integer value is within the valid range (0~0xFFFF)
                if not (0 <= int_value <= 0xFFFF):
                    self.register_error(self.hextets_digits_size_message)

            except ValueError:
                self.register_error(self.hextets_digits_size_message)
