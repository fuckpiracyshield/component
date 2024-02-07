from piracyshield_component.validation.rule import Rule

from ipaddress import ip_network, AddressValueError, NetmaskValueError

class CIDRSyntaxIPv6(Rule):

    """
    Rule that checks for a valid IPv6 CIDR syntax.
    """

    message = 'IPv6 CIDR syntax not valid'

    def __init__(self):
        """
        Initialize parent __init__.
        """
        super().__init__()

    def __call__(self, value: str) -> bool:
        """
        Checks the validity of the passed string.

        :param value: a valid CIDR syntax string.
        """
        try:
            if '/' not in value:
                self.register_error(self.message)

                return False

            network = ip_network(value, strict=False)

            # Check for valid prefix length
            if not (1 <= network.prefixlen <= 128):
                self.register_error(self.message)

                return False

            # If all checks pass
            return True

        except (ValueError, AddressValueError, NetmaskValueError):
            self.register_error(self.message)

            return False

