import traceback

from piracyshield_component.log.logger import Logger

class ApplicationException(Exception):

    """
    Global application exception.
    This class is invoked as a last gateway from the error.
    """

    def __init__(self, code: str, message: str, unrecovered_exception = None):
        """
        Provides context for the exception.

        :param code: predefined code that identifies the error.
        :param message: short description of the issue.
        """

        self._code = code

        self._message = message

        self._unrecovered_exception = unrecovered_exception

        logger = Logger('application')

        logger.debug(f'{code}: {message}')

        if unrecovered_exception:
            self._traceback = traceback.format_exc()

            logger.error(f'Unrecovered exception: {unrecovered_exception} {self._traceback}')

    @property
    def code(self) -> str:
        """
        Sets the options.

        :return: string containing the error code.
        """

        return self._code

    @property
    def message(self) -> str:
        """
        Sets the options.

        :return: string of the error message.
        """

        return self._message
