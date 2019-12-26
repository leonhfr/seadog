from .barchart import Barchart
from .distplot import Distplot
from .heatmap import Heatmap
from .histogram import Histogram
from .scatterplot import Scatterplot

class GraphManager:
    def switch(graph_type):
        switcher = {
            'barchart': Barchart,
            'distplot': Distplot,
            'heatmap': Heatmap,
            'histogram': Histogram,
            'scatterplot': Scatterplot
        }
        return switcher.get(graph_type)

    def validate_args(df, args):
        if args['graph_type'] == None:
            return 'Seadog requires a graph type to be specified.'

        if args['x_axis'] == None and args['y_axis'] == None:
            return 'Seadog requires at least one axis to be defined.'

        cols = df.columns.tolist()
        if args['x_axis'] != None and not args['x_axis'] in cols:
            return str.format("Column {} for X axis is not defined in dataset.", args['x_axis'])

        
        if args['x_axis'] != None and not args['x_axis'] in cols:
            return str.format("Column {} for X axis is not defined in dataset.", args['x_axis'])

        return None