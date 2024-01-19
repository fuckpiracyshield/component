from piracyshield_component.validation.rule import Rule

class Length(Rule):

    """
    Rule that checks the length of a value.
    """

    message = 'The value must be comprised between {} and {} characters'

    minimum = None

    maximum = None

    def __init__(self, minimum: int, maximum: int):
        """
        Initialize parent __init__ and set the minimum and maximum allowed length.
        """

        super().__init__()

        self.minimum = minimum

        self.maximum = maximum

    def __call__(self, value: any) -> None:
        """
        Check if our value has the correct specified length.

        param: value: a valid string.
        """

        # TODO: might want to handle this in depth.
        length = len(value) if isinstance(value, str) else len(str(value))

        if length < self.minimum or length > self.maximum:
            self.register_error(self.message.format(self.minimum, self.maximum))
