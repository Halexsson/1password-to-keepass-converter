"""This module contains configurations."""

# Relative file paths.
IN_FILE = "onepassword_data.txt"
OUT_FILE = "keepass_data.csv"
LOG_FILE = "log.txt"

# These are the default fields that are read from
# when importing a CSV file to KeePass.
# Fields not included in the blacklists are grouped into notes.
FIELDS = [
    "group",
    "title",
    "username",
    "password",
    "website",
    "notes"
]

# Keys matching these fields will not be imported
# from the 1password text file.
KEY_BLACKLIST = [
    "uuid",
    "category",
    "ainfo",
    "scope",
    "autosubmit",
]

# Values matching these fields will not be imported
# from the 1password text file.
VAL_BLACKLIST = [
    "Related Items"
]
