from piracyshield_component.validation.rule import Rule

class String(Rule):

    """
    Rule that checks if a string has valid characters.
    """

    message = 'The value must be a string containing letters, numbers'

    message_string = 'The value must be a valid string'

    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    def __init__(self, allowed: str = ''):
        """
        Initialize the parent __init__.

        TODO: we might want to extend this to allow a full customization of the characters list
        (ie. when we don't really want all the characters spectrum)

        :param allowed: a string containing allowed characters other than the default ones.
        """

        super().__init__()

        # join the allowed characters to our main list and convert them to a unique values dictionary
        self.characters = set(''.join([allowed, self.characters]))

    def __call__(self, value: any) -> None:
        """
        Stores and executes the code.

        param: value: a valid string.
        """

        self.value = value

        self.has_characters()

    def has_characters(self) -> None:
        """
        Checks if the value is a valid string instance and if the characters are allowed.
        """

        if not isinstance(self.value, str):
            self.register_error(self.message_string)

        else:
            # converts the value into a dictionary with no duplicates
            exploded_value = set(self.value)

            # check if the characters appear in our list
            if exploded_value.issubset(self.characters) == False:
                self.register_error(self.message)
