# 1password to KeePass Converter
Python solution that aims to convert exported text files from 1Password to KeePass-friendly CSV files.

It is able to convert all of 1password's categories from an exported text file, and automatically categorize them into a CSV file that KeePass can easily interpret and import with the default settings.

# To run the solution
Execute onepassword_to_keepass_converter.py. The default filename for the exported 1password text file is onepassword_data.txt, this can be changed in constants.py along with other settings, such as fields to import and blacklists.

# Make sure to 
Mark the first row as field titles when importing to KeePass. The solution's default configuration groups all custom fields from 1password entries into notes, in order to grant compability.
