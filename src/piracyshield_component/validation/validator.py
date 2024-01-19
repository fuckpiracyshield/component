from __future__ import annotations

from piracyshield_component.validation.rule import Rule

class Validator:

    """
    Validation utility class.
    """

    value = None

    rules = None

    errors = []

    def __init__(self, value, rules: list):
        """
        Sets the options.

        :param value: the value we want to analyze.
        :param rules: a list of validation rule classes.
        """

        self.value = value

        self.rules = rules

        self.errors = []

        self._check_rules()

    def validate(self) -> None:
        """
        Cycles through the set rules collecting errors, if any.
        """

        for rule in self.rules:
            rule(self.value)

            # merge the errors lists
            self.errors = self.errors + rule.errors

    def is_valid(self) -> list | bool:
        """
        Returns true when the errors array is filled.
        """

        return not self.errors

    def _check_rules(self) -> None | Exception:
        """
        Ensures the validity of the passed rules.
        """

        for rule in self.rules:
            if not isinstance(rule, Rule):
                raise ValidatorRuleNonValidException()

            # reset errors on each validation
            rule.errors = []

class ValidatorRuleNonValidException(Exception):

    """
    Raised if the class doesn't inherit the Rule class.
    """

    pass
