import click
import pandas as pd

from .graphs.barchart import Barchart
from .graphs.distplot import Distplot
from .graphs.histogram import Histogram
from .na import Na
from .output import Output
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

    Output.csv(output, output_df)

@cli.command()
@click.option('--x-axis', '-x', type = click.STRING, required = True,
              help = 'Defines the column to plot on the X axis')
@click.option('--log', '-l', is_flag = True, help = 'Axis transformation to logarithmic scale')
@click.option('--output', '-o', is_flag = False,
    type=click.File('wb'),
    help = 'Defines output file; use - for stdout. If not set, Seadog will attempt to open the graph with the default image viewer.')
# TODO: size option
# TODO: rotate option
@click.pass_context
def barchart(ctx, x_axis, log, output):
    """Draws a bar chart. Used to plot the distribution of a categorical variable."""
    dataframe = ctx.obj['CSV']
    image = Barchart.make(dataframe, x_axis, log)
    Output.png(output, image)

@cli.command()
@click.option('--x-axis', '-x', type = click.STRING, required = True,
              help = 'Defines the column to plot on the X axis')
@click.option('--bucket', '-b', type = click.FLOAT,
              help = 'Overrides the computed bucket size.')
@click.option('--output', '-o', is_flag = False,
    type=click.File('wb'),
    help = 'Defines output file; use - for stdout. If not set, Seadog will attempt to open the graph with the default image viewer.')
# TODO: size option
# TODO: rotate option
@click.pass_context
def distplot(ctx, x_axis, bucket, output):
    """Draws a distribution plot. Used to plot the distribution of a numerical variable."""
    dataframe = ctx.obj['CSV']
    image = Distplot.make(dataframe, x_axis, bucket)
    Output.png(output, image)

@cli.command()
@click.option('--x-axis', '-x', type = click.STRING, required = True,
              help = 'Defines the column to plot on the X axis')
@click.option('--bucket', '-b', type = click.FLOAT,
              help = 'Overrides the computed bucket size.')
@click.option('--log', '-l', is_flag = True, help = 'Axis transformation to logarithmic scale')
@click.option('--discrete', '-d', is_flag = True, help = "Makes the plot discrete.")
@click.option('--output', '-o', is_flag = False,
    type=click.File('wb'),
    help = 'Defines output file; use - for stdout. If not set, Seadog will attempt to open the graph with the default image viewer.')
# TODO: size option
# TODO: rotate option
@click.pass_context
def histogram(ctx, x_axis, bucket, log, discrete, output):
    """Draws a histogram. Used to plot the distribution of a numeric variable."""
    dataframe = ctx.obj['CSV']
    image = Histogram.make(dataframe, x_axis, bucket, log, discrete)
    Output.png(output, image)

if __name__ == '__main__':
    cli(obj = {})