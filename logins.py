"""This module contains the class for importing
and then exporting logins from 1password to KeePass.
"""

from constants import (IN_FILE, OUT_FILE, FIELDS, KEY_BLACKLIST,
                       VAL_BLACKLIST)
from log import write_log
from reader import read_text_file

class Logins:
    """This class holds the methods for importing, and exporting logins."""

    logins = {}

    def import_file(self):
        """Imports a read text file and
        re-structures paragraphs to logins based on filters.
        """

        entries = read_text_file(IN_FILE)

        for entry in entries:
            write_log("Importing entry {0} of {1}"
                      .format(entries.index(entry) + 1, len(entries)))

            login = {
                "group": "logins",
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

                    # Only add to the login if the key isn't empty.
                    if not key:
                        continue

                    if (key in FIELDS and
                            key not in login):
                        login[key] = val
                    else:
                        if (key not in KEY_BLACKLIST and
                                val not in VAL_BLACKLIST and
                                content not in login["misc"]):
                            login["misc"].append(key + "=" + val)
                except IndexError:

                    # Line is part of a note.
                    login["misc"].append(content.strip("\""))

            # Add remaining fields to the login as notes.
            login["notes"] = "\n".join("{0}".format(content)
                                       for content in login["misc"])

            if len(entry) > 2:

                # Add the login to the logins by it's title.
                if login["title"] not in self.logins:
                    self.logins[login["title"]] = login
                else:

                    # If the title already exists,
                    # it's probably another account for the same service.
                    login["duplicates"] += 1
                    duplicate_title = "{0} {1}"\
                            .format(login["title"], login["duplicates"])
                    self.logins[duplicate_title] = login
            else:
                write_log("Empty entry '{0}' skipped.".format(entry))

        print("Imported {0} entries from {1}."
              .format(len(self.logins), IN_FILE))

    def export_file(self):
        "Creates and writes a CSV file to be imported in KeePass."

        with open(OUT_FILE, "w") as file:
            field_names = ",".join("{0}".format(field) for field in FIELDS)
            file.write(field_names + "\n")

            login_idx = 0

            for login in self.logins:
                login_idx += 1
                write_log("Exporting {0} ({1} of {2})"
                          .format(login, login_idx, len(self.logins)))

                values = []

                for field in FIELDS:
                    try:
                        values.append(self.logins[login][field])
                    except KeyError:

                        # If a key is missing, add it with an empty value.
                        write_log("Login: {0} is missing the field: {1}.\
 Adding empty value."
                                  .format(login, field))
                        values.append("")

                # Wrap each value in quotation marks
                entry = ",".join("\"{0}\"".format(val) for val in values)

                file.write(entry + "\n")

        print("Exported {0} logins to {1}."
              .format(len(self.logins), OUT_FILE))
