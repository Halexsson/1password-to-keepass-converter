"""This module contains the function for importing
entries from 1password to KeePass.
"""

from constants import IN_FILE, FIELDS, KEY_BLACKLIST, VAL_BLACKLIST
from log import write_log

def import_entries(data):
    """Imports a dictionary of arrays and
    re-structures paragraphs to entries based on filters.
    """

    entries = {}

    for entry in data:
        write_log("Importing entry {0} of {1}"
                  .format(data.index(entry) + 1, len(data)))

        paragraph = {
            "group": "",
            "notes": "",
            "misc": [],
            "duplicates": 0
        }

        entry = entry.split("\n")

        for line in entry:

            # Remove empty space from the line.
            content = line.strip("\r\n")

            # If the line isn't blank,
            # split the content once into key and value.
            if len(content) < 2:
                continue

            try:
                key_val = content.split("=", 1)
                key = key_val[0].strip("\"").lower()
                val = key_val[1].strip("\"")

                # Only add to the entry if the key isn't empty.
                if not key:
                    continue

                if (key in FIELDS and
                        key not in paragraph):
                    paragraph[key] = val
                else:
                    if (key not in KEY_BLACKLIST and
                            val not in VAL_BLACKLIST and
                            content not in paragraph["misc"]):
                        paragraph["misc"].append(key + "=" + val)
            except IndexError:

                # Line is part of a note.
                paragraph["misc"].append(content.strip("\""))

        # Add remaining fields to the entry as notes.
        paragraph["notes"] = "\n".join("{0}".format(content)
                                       for content in paragraph["misc"])

        if len(entry) > 2:

            # Add the entry to the entries by it's title.
            if paragraph["title"] not in entries:
                entries[paragraph["title"]] = paragraph
            else:

                # If the title already exists,
                # it's probably another account for the same service.
                paragraph["duplicates"] += 1
                duplicate_title = "{0} {1}"\
                        .format(paragraph["title"], paragraph["duplicates"])
                entries[duplicate_title] = paragraph
        else:
            write_log("Empty entry '{0}' skipped.".format(entry))

    print("Imported {0} entries from {1}."
          .format(len(entries), IN_FILE))

    return entries
