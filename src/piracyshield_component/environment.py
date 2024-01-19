import os

# TODO: provide development and production environment types
# to have customization of the code in the other packages.

class Environment:

    """
    Environment management.

    DATA_PATH consists in the root of the next folders.
    The structure should be:

        data/
            config/
            cache/
    """

    DATA_PATH = os.environ['PIRACYSHIELD_DATA_PATH']

    CONFIG_PATH = os.environ['PIRACYSHIELD_CONFIG_PATH']

    CACHE_PATH = os.environ['PIRACYSHIELD_CACHE_PATH']
