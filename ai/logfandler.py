import logging
import os

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

def get_logger(name: str) -> logging.Logger:
    """
    Create and return a logger with the given name.
    Supports separate loggers and avoids duplicate handlers.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if logger.handlers:
        return logger  # Avoid adding handlers multiple times

    # === INFO Handler ===
    info_handler = logging.FileHandler(os.path.join(LOG_DIR, f"{name}_info.log"))
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(logging.Formatter('%(asctime)s - INFO - %(message)s'))
    info_handler.addFilter(lambda record: record.levelno == logging.INFO)

    # === ERROR Handler ===
    error_handler = logging.FileHandler(os.path.join(LOG_DIR, f"{name}_error.log"))
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(logging.Formatter('%(asctime)s - ERROR - %(message)s'))

    logger.addHandler(info_handler)
    logger.addHandler(error_handler)

    return logger