import click
import pandas as pd
from icecream import ic


@click.command()
@click.option("--in", "-i", "in_file", required=True,help="Path to csv file to be processed.")
@click.option("--out-file", "-o", default="./output.xlsx",help="Path to excel file to store the result.")



def process(in_file, out_file):
    """
    Processes the input file IN and stores the result to
    output file OUT.
    """
    input = csv_read(in_file)
    ic(input)
    output = process_csv(input)
    ic(output)
    write_excel(output, out_file)


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

if __name__ =="__main__":
    process()