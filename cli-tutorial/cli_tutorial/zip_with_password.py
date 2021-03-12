import click
import pandas as pd
from icecream import ic
from funcy import identity
import os
from datetime import datetime
import zipfile as zf


def zip_file(in_file,out_file, user, password):

    with zf.ZipFile(in_file) as myzip:
        fname = myzip.namelist()
        with myzip.open(fname[0],pwd = bytes(password, 'utf-8')) as myfile:
            ic(myfile.read())

@click.command()
@click.option("--in", "-i", "in_file", required=True,help="Path to csv file to be processed.",
    type=click.Path(exists=True, dir_okay=False, readable=True),)
@click.option("--out", "-o","out_file", default="/home/ragav/GITdir/command_line_interface/cli-tutorial/cli_tutorial/test/output.zip",
    help="Path to excel file to store the result.",type=click.Path(dir_okay=False),)
@click.option('--user', prompt=True,
              default=lambda: os.environ.get('USER', ''))
@click.password_option()

def process(in_file, out_file,user, password):
    """
    Reading zip file with a password protetion. The function asks for user name and password.
    User name is connected with any access rights. Password for the opening of zip file
    the password for the zip file is 1234
    """

    ic(os.environ['USER'])
    #click.echo(os.environ['USER'])
    zip_file(in_file,out_file, user, password)

if __name__ =="__main__":
    process()