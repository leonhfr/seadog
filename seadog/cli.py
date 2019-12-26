import click
import pandas as pd
import termplotlib

from .na import Na
from .graphs.graph_manager import GraphManager
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

    _output(output, output_df)

@cli.command()
# Graph type feature switch
# @click.option('--barchart', 'graph_type', flag_value='barchart',
#               help = 'Draws a barchart')
# @click.option('--distplot', 'graph_type', flag_value='distplot',
#               help = 'Draws a distribution plot')
@click.option('--histogram', 'graph_type', flag_value='histogram',
              help = 'Draws a histogram')
# @click.option('--scatterplot', 'graph_type', flag_value='scatterplot',
#               help = 'Draws a scatter plot')
# @click.option('--heatmap', 'graph_type', flag_value='heatmap',
#               help = 'Draws a heatmap')
# Data definition
@click.option('--x-axis', '-x', type = click.STRING,
              help = 'Defines the column to plot on the X axis')
@click.option('--y-axis', '-y', type = click.STRING,
              help = 'Defines the column to plot on the Y axis')
@click.option('--output', '-o', is_flag = False,
    type=click.File('wb'),
    help = 'Defines output file; use - for stdout. If not set, Seadog will attempt to open the graph with the default image viewer.')
@click.option('--logx/--no-logx', help = 'X-axis transformation to logarithmic scale')
@click.option('--logy/--no-logy', help = 'Y-axis transformation to logarithmic scale')
# Graph CLI
@click.pass_context
def graph(ctx, graph_type, x_axis, y_axis, logx, logy, output):
    dataframe = ctx.obj['CSV']

    args = { 'graph_type': graph_type,
              'x_axis': x_axis,
              'y_axis': y_axis,
              'logx': logx,
              'logy': logy }
    print(args) # TODO: Remove this

    err = GraphManager.validate_args(dataframe, args)
    if err != None:
        ctx.fail(err)

    graph = GraphManager.switch(graph_type)
    err = graph.validate(dataframe, args)
    if err != None:
        ctx.fail(err)

    # TODO: Handle graph output
    click.echo(graph.output(dataframe, args))
    # _output(output, output_df)

def _output(output, dataframe):
    # TODO: handle this in chunks?
    # TODO: handle image viewer opening if output is None
    output_csv = dataframe.to_csv()
    output.write(output_csv.encode('utf-8'))
    output.flush()

if __name__ == '__main__':
    cli(obj = {})