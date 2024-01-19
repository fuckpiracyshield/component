from piracyshield_component.environment import Environment

import os
import toml

class Config:

    """
    Configuration utility that supports TOML config creation.
    """

    config_path = None

    config_content = None

    def __init__(self, config_path: str):
        """
        Handles the setting of the path of a config file.
        This is representable by: Environment.CONFIG_PATH/<config_path>/my_config.toml

        :param config_path: a valid path present in CONFIG_PATH directory.
        """

        self.config_path = config_path

        self.config_content = self.load()

    def load(self) -> dict | Exception:
        """
        Loads the whole file.

        :return: returns the content of the file.
        """

        file_path = f'{Environment.CONFIG_PATH}/{self.config_path}.toml'

        try:
            return toml.load(file_path)

        except FileNotFoundError:
            raise ConfigNotFound(f'Impossibile trovare file {file_path}')

    def get(self, key: str) -> str | Exception:
        """
        Gets a single key from the loaded content.

        :param key: a valid key.
        :return: value of the dictionary key.
        """

        try:
            return self.config_content[key]

        except KeyError:
            raise ConfigKeyNotFound(f'Impossibile trovare chiave {key}')

    def get_all(self, key: str = None) -> any:
        """
        Returns the whole content of a configuration or its path.

        :return: different types of data.
        """

        return self.config_content[key] if key else self.config_path

class ConfigNotFound(Exception):

    """
    No config found.
    """

    pass

class ConfigKeyNotFound(Exception):

    """
    Key passed not found.
    """

    pass
