import click

'''
@click.command()
def hello():
    click.echo('Hello World!')

@click.group()
def cli():
    pass

@click.command()
def initdb():
    click.echo('Initialized the database')

@click.command()
def dropdb():
    click.echo('Dropped the database')


@click.command()
@click.option('-c','--count', default=1, help='number of greetings')
@click.argument('name')
def cli(count, name):
    for x in range(count):
        click.echo('Hello %s!' % name)
'''

def inout(input, output):
    """Copy contents of INPUT to OUTPUT."""
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(chunk)


@click.command()
@click.argument('input', type=click.File('rb'))
@click.argument('output', type=click.File('wb'))
def cli(input,output):
    inout(input,output)

if __name__ == '__main__':
    cli()



