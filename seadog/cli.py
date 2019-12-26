import click
import pandas as pd
import termplotlib

from .na import Na
from .stats import Stats

@click.group()
@click.argument('input', type = click.File('rb'))
@click.pass_context
def cli(ctx, input):
    ctx.ensure_object(dict)
    # TODO: try/catch? input may fail
    csv = pd.read_csv(input)
    ctx.obj['CSV'] = csv
    
@cli.command()
@click.pass_context
def describe(ctx):
    dataframe = ctx.obj['CSV']
    description = Stats.get_description(dataframe)
    click.echo(description)

@cli.command()
@click.pass_context
@click.argument('n', required = False, default = 5)
def sample(ctx, n):
    dataframe = ctx.obj['CSV']
    sample = Stats.get_sample(dataframe, n)
    click.echo(sample)

@cli.command()
@click.pass_context
def correlation(ctx):
    dataframe = ctx.obj['CSV']
    correlation = Stats.get_correlation(dataframe)
    click.echo(correlation)

@cli.command()
@click.option('--total', '-t', is_flag = True, 
    help = 'Include total count of elements in graph')
@click.option('--remove-cols', '-c', is_flag = True, 
    help = 'Remove columns which contain missing data')
@click.option('--remove-rows', '-r', is_flag = True, 
    help = 'Remove rows which contain missing data')
@click.option('--output', '-o', is_flag = False,
    type=click.File('wb'),
    help = 'Defines output file, use - for stdout.')
@click.pass_context
def na(ctx, total, remove_cols, remove_rows, output):
    dataframe = ctx.obj['CSV']
    na_stats = Na.get_na(dataframe, total)
    
    output_df = pd.DataFrame(data = {})

    if remove_rows == True or remove_cols == True:
        output_df = Na.remove_na(dataframe, remove_rows, remove_cols)
        diff = Na.get_diff(dataframe, output_df)
        na_stats += '\n' + diff

    if output == None:
        click.echo(na_stats)
        return

    # TODO: handle this in chunks?
    output_csv = output_df.to_csv()
    output.write(output_csv.encode('utf-8'))
    output.flush()

if __name__ == '__main__':
    cli(obj = {})