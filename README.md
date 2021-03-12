# command_line_interface

Click is used to prepare command line interface (CLI). 
cli-tutorial/cli_tutorial/cli.py - contains the commands for reading data, some data transformation, saving the data to excel.
The file could be saved to a specific place or ever server with a username and password prompts.
Additional options could be specified as adding a choice for a file saving path. There is no ned to type the whole path in. 

cli-tutorial/cli_tutorial/zip_with_password.py - if a zip is saved with password. The username and password is prompted to open the file.

cli-tutorial/cli_tutorial/baza.py - represent some basic usage.

cli-tutorial/pyproject.toml  contains poetry scrips

cli = 'cli_tutorial.cli:process'
zwp = 'cli_tutorial.zip_with_password:process'
baza = 'cli_tutorial.baza:cli'

executed with command like "poetry run baza cli_tutorial/vol_per_year.csv"
