import os

class Filesystem:

    """
    Class to manage elements on the filesystem.
    """

    def get_size(self, absolute_file_path) -> int | Exception:
        """
        Returns the size in Bytes format.

        :param file_path: the absolute path of the file.
        """

        if os.path.exists(absolute_file_path):
            return os.path.getsize(absolute_file_path)

        else:
            raise FilesystemNotFoundException()

class FilesystemNotFoundException(Exception):

    """
    Element not found in the filesystem.
    """

    pass
