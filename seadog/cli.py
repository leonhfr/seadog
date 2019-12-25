import click
import pandas as pd
import termplotlib
from tabulate import tabulate

@click.command()
@click.argument('input', type=click.File('rb'))
@click.option('--describe','-d',is_flag=True,help='Describe the data.')
def cli(input,describe):
    dataframe = pd.read_csv(input)
    if (describe):
        _describe(dataframe)
    else:
        click.echo('No options.')

def _describe(dataframe):
    df = dataframe.describe()
    table = tabulate(df, headers = df.columns, numalign = 'right')
    click.echo(table)

if __name__ == '__main__':
    cli()