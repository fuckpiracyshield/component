from abc import ABC, abstractmethod

class Rule(ABC):

    """
    Basic rule class.
    """

    errors = []

    def __init__(self):
        """
        Initialize errors list.
        """

        self.errors = []

    @abstractmethod
    def __call__(self):
        """
        Method invoked for the rule processing.
        """

        pass

    def register_error(self, message) -> None:
        """
        Registers all of the errors occurred during the validation.

        :param message: error message.
        """

        self.errors.append(message)
