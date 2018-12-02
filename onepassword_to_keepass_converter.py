#!/usr/bin/env python
"""This solution aims to convert text files exported
by 1Password to KeePass-friendly CSV files.

Filenames, fields, and blacklists can be configured in constants.py.
"""

from log import clear_log
from constants import IN_FILE
from read_data import read_file
from import_data import import_entries
from export_data import export_entries

__author__ = "Alexander Hansson"
__copyright__ = "Copyright 2018, Alexander Hansson"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Alexander Hansson"
__Email__ = "10744667+halexsson@users.noreply.github.com"
__status__ = "Prototype"

def run():
    """This function executes the solution."""

    # Begin by creating a new, or overwriting a previous log.
    clear_log()

    # Read entries from a 1password text file.
    read_entries = read_file(IN_FILE)

    # Import entries from a 1password text file.
    imported_entries = import_entries(read_entries)

    # Export entries to a CSV file for KeePass.
    export_entries(imported_entries)

    # Let the user know that the solution has finished successfully.
    print("Done.")

run()
