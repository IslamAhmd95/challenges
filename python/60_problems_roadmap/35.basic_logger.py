"""
Problem:
    Create a simple logger function that takes a message string and appends it to a log file along with a timestamp. The function should ensure that old messages remain in the file (append mode), not overwritten.
"""
import logging
import os

logger = logging.getLogger(__name__)
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log.txt')
logging.basicConfig(filename=path,
    level=logging.INFO,
    format="%(name)s - %(levelname)s - [%(asctime)s] - %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S')  # name is for logger name which is the module or file name


def log_message(message):
    try:
        logger.info(message)
        print("All fine")
    except Exception as e:
        print(f"Logging failed: {e}")

log_message("User login successful")
log_message("User performed action X")
