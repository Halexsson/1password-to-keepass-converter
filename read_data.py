"""This module contains the function for
reading text files exported from 1password.
"""

def read_file(in_file):
    """Returns new dictionary of arrays with lines, split in paragraphs.

    input_file: Text file that should be split.
    """

    data = open(in_file, "r").read()
    entries = data.split("\n\n")

    print("Read {0} entries from {1}".format(len(entries), in_file))

    return entries
