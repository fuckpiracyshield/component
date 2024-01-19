from piracyshield_component.utils.time import Time

import logging

class FilesystemOutput(logging.FileHandler):

    """
    Manages filesystem output.
    """

    FORMAT = "%d-%m-%Y"

    def __init__(self, name: str, path: str, format_syntax: str):
        """
        Sets the output options.

        :param name: the filename of the log.
        :param path: absolute path of the logging directory.
        :param format_syntax: formatting string style.
        """

        super().__init__(self._get_filename(name, path))

        self.setFormatter(logging.Formatter(format_syntax))

    def _get_filename(self, name: str, path: str) -> str:
        """
        Resolves the file position.

        :param name: the filename of the log.
        :param path: absolute path of the log.
        :return: absolute filename path.
        """

        now = Time.now_format(self.FORMAT)

        return f'/{path}/{now}-{name}.log'
