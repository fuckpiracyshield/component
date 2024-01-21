from piracyshield_component.validation.rule import Rule

import ipaddress

class CIDRSyntaxIPv4(Rule):

    """
    Rule that checks for a valid IPv4 CIDR syntax.
    """

    message = 'IPv4 CIDR syntax not valid'

    def __init__(self):
        """
        Initialize parent __init__.
        """

        super().__init__()

    def __call__(self, value: str) -> None:
        """
        Checks the validity of the passed string.

        :param value: a valid CIDR syntax string.
        """

        try:
            # doesn't seem solid enough, but we're not too paranoid
            if '/' not in value:
                self.register_error(self.message)

                return False

            network = ipaddress.ip_network(value, strict = True)

            # make sure we have at least one address
            if network.num_addresses < 1:
                self.register_error(self.message)

                return False

        # non valid at all
        except ValueError:
            self.register_error(self.message)

            return False
