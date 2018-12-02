"""This module contains functions for clearing and writing a log."""

from constants import LOG_FILE

def clear_log():
    """Clears the log by overwriting it."""

    with open(LOG_FILE, "w") as file:
        file.write("Log\r\n")
        print("Cleared {0}.".format(LOG_FILE))

def write_log(message):
    """Writes to the log.

    message: What should be written to the log.
    """

    with open(LOG_FILE, "a") as file:
        file.write(message + "\n")
