import os
import logging


def custom_logger():
    """
    Function to generate and return a custom logger for
    a specific module from which this function was called.

    Returns
    -------
    logger: Object
        Customer logger.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    logFormatter = logging.Formatter(
        '%(levelname)s - %(asctime)s\n %(message)s\n\n')

    filename = "logs.out"
    log_directory = ".//..//logs"
    os.makedirs(log_directory, exist_ok=True)
    filepath = os.path.join(log_directory, filename)

    fileHandler = logging.FileHandler(filepath)
    fileHandler.setFormatter(logFormatter)

    logger.addHandler(fileHandler)
    return logger


logger = custom_logger()
