from piracyshield_component.validation.rule import Rule

class Required(Rule):

    """
    Rule that checks if a string is empty.
    """

    message = 'A valid string is required'

    def __init__(self):
        """
        Initialize parent __init__.
        """

        super().__init__()

    def __call__(self, value: any) -> None:
        """
        Stores and executes the code.

        param: value: any value.
        """

        self.value = value

        self.is_empty()

    def is_empty(self) -> None:
        """
        Check if the string is empty.
        No filters are applied in this phase as we want to avoid input and output misalignements.
        """

        if not self.value:
            self.register_error(self.message)
