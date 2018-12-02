"""This module contains the function for
exporting entries from 1password to KeePass.
"""

from constants import OUT_FILE, FIELDS
from log import write_log

def export_entries(data):
    """Creates and writes a CSV file to be imported in KeePass.

    entries: 1password data imported by the solution.
    """

    with open(OUT_FILE, "w") as file:
        field_names = ",".join("{0}".format(field) for field in FIELDS)
        file.write(field_names + "\n")

        entry_idx = 0

        for entry in data:
            entry_idx += 1
            write_log("Exporting {0} ({1} of {2})"
                      .format(entry, entry_idx, len(data)))

            values = []

            for field in FIELDS:
                try:
                    values.append(data[entry][field])
                except KeyError:

                    # If a key is missing, add it with an empty value.
                    write_log("Entry: {0} is missing the field: {1}.\
Adding empty value."
                              .format(entry, field))
                    values.append("")

            # Wrap each value in quotation marks
            entry = ",".join("\"{0}\"".format(val) for val in values)

            file.write(entry + "\n")

    print("Exported {0} entries to {1}."
          .format(len(data), OUT_FILE))
