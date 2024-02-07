from piracyshield_component.validation.rule import Rule

class IPv4(Rule):

    """
    Rule that checks for a valid IPv4.
    """

    octets_message = 'IPv4 not valid, expecting four octects, got {}'

    octets_digits_message = 'IPv4 not valid, expecting four octets of digits'

    octets_length_message = 'IPv4 not valid, one or more octet(s) too long'

    octets_digits_size_message = 'IPv4 not valid, expecting digits from 0 to 255'

    def __init__(self):
        """
        Initialize parent __init__.
        """

        super().__init__()

    def __call__(self, value: str) -> None:
        """
        Checks the validity of the passed string.
        Instead of relying on regular expression, is it better to check the single octects.
        This also allow for better error reporting.

        :param value: a valid string.
        """

        octets = value.split('.')

        octets_size = len(octets)

        # we're expecting 4 octects
        if octets_size != 4:
            self.register_error(self.octets_message.format(octets_size))

            return False

        for octet in octets:
            single_octet_size = len(octet)

            # each octect must be an integer
            if not octet.isdigit():
                self.register_error(self.octets_digits_message)

                return False

            # with a maximum length of 3
            if single_octet_size > 3:
                self.register_error(self.octets_length_message)

                return False

            int_octet = int(octet)

            # between 0 and 255
            if int_octet < 0 or int_octet > 255:
                self.register_error(self.octets_digits_size_message)

                return False
