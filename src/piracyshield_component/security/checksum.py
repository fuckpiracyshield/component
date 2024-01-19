from __future__ import annotations

import hashlib

class Checksum:

    """
    Helper class for checksum calculations.
    """

    def from_string(self, algorithm: str, string: str) -> str:
        """
        Calculates checksum of a given string.

        :param str: the string to process.
        :return: checksum string.
        """

        try:
            instance = hashlib.new(algorithm)

            # convert the string into bytes before handling
            instance.update(bytes(string, 'utf-8'))

        except ValueError:
            raise ChecksumParameterException()

        except UnicodeEncodeError:
            raise ChecksumUnicodeException()

        except AttributeError:
            raise ChecksumParameterException()

        return instance.hexdigest()

    def from_file(self, algorithm: str, file_path: str) -> str:
        """
        Calculates checksum of a given file.

        :param str: the absolute file path.
        :return: checksum string.
        """

        try:
            instance = hashlib.new(algorithm)

            with open(file_path, 'rb') as handle:
                while True:
                    data = handle.read(65536)

                    # EOF
                    if not data:
                        break

                    instance.update(data)

            return instance.hexdigest()

        except ValueError:
            raise ChecksumParameterException()

        except AttributeError:
            raise ChecksumParameterException()

        except:
            raise ChecksumCalculationException()

class ChecksumCalculationException(Exception):

    """
    Cannot process the file.
    """

    pass

class ChecksumUnicodeException(Exception):

    """
    Cannot encode the data to UTF-8.
    """

    pass

class ChecksumParameterException(Exception):

    """
    Most likely not a string.
    """

    pass
