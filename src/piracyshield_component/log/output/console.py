import logging
import sys

from piracyshield_component.log.formatter import ColorFormatter

class ConsoleOutput(logging.StreamHandler):

    """
    Manages the console output.
    """

    def __init__(self, format_syntax: str, colorize: bool = True):
        """
        Sets the output options.

        :param format_syntax: the string format to apply.
        :param colorize: whether to apply or not colorization of the output.
        """

        super().__init__(stream = sys.stdout)

        formatter = None

        if colorize == True:
            formatter = ColorFormatter(format_syntax)

        else:
            formatter = logging.Formatter(format_syntax)

        self.setFormatter(formatter)
