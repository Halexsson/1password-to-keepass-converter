#!/usr/bin/env python
"""This solution aims to convert text files exported
by 1Password to KeePass-friendly CSV files.

Filenames, fields, and blacklists can be configured in constants.py.
"""

from logins import Logins
from log import clear_log

__author__ = "Alexander Hansson"
__copyright__ = "Copyright 2018, Alexander Hansson"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Alexander Hansson"
__Email__ = "10744667+halexsson@users.noreply.github.com"
__status__ = "Prototype"

def run():
    """This function executes the solution."""

    # Instantiate the logins class.
    logins = Logins()

    # Begin by creating or overwriting a previous log.
    clear_log()

    # Import logins from a 1password text file.
    logins.import_file()

    # Export logins to a CSV file for KeePass.
    logins.export_file()

    # Let the user know that the solution has finished successfully.
    print("Done.")

run()
