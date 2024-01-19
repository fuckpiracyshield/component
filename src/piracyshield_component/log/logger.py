from __future__ import annotations

from piracyshield_component.environment import Environment
from piracyshield_component.config import Config

from piracyshield_component.log.output.console import ConsoleOutput
from piracyshield_component.log.output.filesystem import FilesystemOutput

import logging

class Logger:

    """
    Application logging management class.
    """

    name = None

    logger = None

    general_config = None

    console_config = None

    filesystem_config = None

    def __init__(self, name: str):
        """
        Initializes a new logging instance using a nem as identifier.

        :param name: a valid string representing the type of service that wants to log the operations.
        """

        self._prepare_configs()

        self.name = name

        self.logger = logging.getLogger(name)

        self.logger.setLevel(self._get_level(self.general_config['level']))

        self._register_handlers()

    def _register_handlers(self) -> None:
        """
        Registers different kind of handlers.

        Supporterd outputs:
            - console
            - filesystem
        """

        if self.console_config['enabled'] == True and not self._has_handler(ConsoleOutput):
            self.logger.addHandler(
                ConsoleOutput(
                    format_syntax = self.general_config['format'],
                    colorize = self.console_config['colorize']
                )
            )

        if self.filesystem_config['enabled'] == True and not self._has_handler(FilesystemOutput):
            self.logger.addHandler(
                FilesystemOutput(
                    name = self.name,
                    path = self.filesystem_config['path'],
                    format_syntax = self.general_config['format']
                )
            )

    def _has_handler(self, instance) -> bool:
        """
        Avoids duplications of the already added handlers.

        :return: true or false if the handler is already present or not.
        """

        return any(isinstance(h, instance) for h in self.logger.handlers)

    def _get_level(self, level: str) -> int | Exception:
        """
        Handles the level based on a fixed list of options.

        :return: the real integer value of the logging levels.
        """

        match level:
            case 'debug':
                return logging.DEBUG

            case 'info':
                return logging.INFO

            case 'warning':
                return logging.WARNING

            case 'error':
                return logging.ERROR

            case 'critical':
                return logging.CRITICAL

            case _:
                raise LoggerLevelNotFound()

    def debug(self, message: str) -> None:
        """
        Handles debugging messages.
        Logs minor informations useful for debugging.

        :param message: the string we want to log.
        """

        self.logger.debug(message)

    def info(self, message: str) -> None:
        """
        Handles info messages.
        Logs ordnary operations.

        :param message: the string we want to log.
        """

        self.logger.info(message)

    def warning(self, message: str) -> None:
        """
        Handles warning messages.
        Logs issues of any kind.

        :param message: the string we want to log.
        """

        self.logger.warning(message)

    def error(self, message: str) -> None:
        """
        Handles error messages.
        Logs recoverable errors.

        :param message: the string we want to log.
        """

        self.logger.error(message)

    def critical(self, message: str) -> None:
        """
        Handles critical messages.
        This should be considered a step before quitting the application.

        :param message: the string we want to log.
        """

        self.logger.critical(message)

    def _prepare_configs(self):
        """
        Register configurations.
        """

        self.general_config = Config('logger').get('general')

        self.console_config = Config('logger').get('console')

        self.filesystem_config = Config('logger').get('filesystem')

class LoggerLevelNotFound(Exception):

    """
    Log level specified is non valid.
    """

    pass
