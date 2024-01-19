import logging

class ColorFormatter(logging.Formatter):

    """
    Manages color output for the console.
    """

    def __init__(self, fmt = None, datefmt = None, style = '%'):
        """
        Defines the final format of the message.

        # TODO: this should be better explained.

        Further info can be found on the official documentation:
            - https://docs.python.org/3/library/logging.html#formatter-objects

        :param fmt: optional format of the string.
        :param datefmt: optional date format of the string.
        :param style: formatting string style.
        """

        super().__init__(fmt = fmt, datefmt = datefmt, style = style)

        self.color_map = {
            logging.DEBUG: Color.DEBUG,
            logging.INFO: Color.INFO,
            logging.WARNING: Color.WARNING,
            logging.ERROR: Color.ERROR,
            logging.CRITICAL: Color.CRITICAL,
        }

        self.reset_color = '\033[0m'

    def format(self, record) -> str:
        """
        Applies formatting to the passed string.

        :param record: string to be formatted.
        :return: the formatted string.
        """

        levelname = record.levelname

        message = super().format(record)

        color = self.color_map.get(record.levelno)

        if color:
            message = color + message + self.reset_color

        return message

class Color:

    """
    Default formatting colors for each logging level.
    """

    DEBUG = '\033[1;37m'

    INFO = '\033[1;32m'

    WARNING = '\033[1;33m'

    ERROR = '\033[1;31m'

    CRITICAL = '\033[1;31m'
