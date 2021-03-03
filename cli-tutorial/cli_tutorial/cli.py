import click
import pandas as pd
from icecream import ic
from funcy import identity
import os


@click.command()
@click.option("--in", "-i", "in_file", required=True,help="Path to csv file to be processed.",
    type=click.Path(exists=True, dir_okay=False, readable=True),)
@click.option("--out", "-o","out_file", default="output.xlsx",help="Path to excel file to store the result.",
    type=click.Path(dir_okay=False),)
@click.option('--verbose', is_flag=True, help="Verbose output")
@click.option("--dev", "server_url", help="Upload to dev server",
    flag_value='/home/ragav/GITdir/command_line_interface/cli-tutorial/cli_tutorial/dev',)
@click.option("--test", "server_url", help="Upload to test server",
    flag_value='/home/ragav/GITdir/command_line_interface/cli-tutorial/cli_tutorial/test',)
@click.option("--prod", "server_url", help="Upload to prod server",
    flag_value='/home/ragav/GITdir/command_line_interface/cli-tutorial/cli_tutorial/prod',default=True)

def process(in_file, out_file,verbose,server_url):
    """
    Processes the input file IN and stores the result to
    output file OUT.
    """

    print_func = print if verbose else identity
    print_func("We will start with the input")
    input = csv_read(in_file)
    if verbose is False:
        ic(input)
    print_func("Next we procees the data")
    output = process_csv(input)
    if verbose is False:
        ic(output)
    print_func("Finally, we dump it")
    write_excel(output, out_file)
    print_func("Upload it to the server")
    upload_to(server_url, output)

def csv_read(path):
    try:
        df = pd.read_csv(path,sep=',')
    except:
        pass

    try:
        df = pd.read_csv(path,sep=';')
    except:
        pass

    return df


def process_csv(input):
    output = input
    return output

def write_excel(output,out_file):
    with pd.ExcelWriter(out_file) as writer:
        output.to_excel(writer)

def upload_to(server_url, output):
    os.path.join('a', 'b', 'c')


if __name__ =="__main__":
    process()