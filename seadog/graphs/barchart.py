from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sb

from .helper import Helper

class Barchart:
    def validate(dataframe, column):
        if column not in dataframe.columns:
            err = "Column '{}' does not exist in dataset.".format(column)
            return err

        return None

    def make(dataframe, column, log, size):
        figsize = Helper.get_figsize(size)
        plt.figure(figsize = figsize)

        x_label = column
        y_label = 'count'
        base_color = sb.color_palette()[0]
        cat_order = dataframe[column].value_counts().index

        sb.countplot(data = dataframe, x = column, color = base_color, order = cat_order)
        plt.xticks(rotation = 90)

        if log:
            y_label = 'log(' + y_label + ')'
            max = plt.ylim()[1]
            ticks = Helper.get_log_ticks(max)
            plt.yscale('log')
            plt.yticks(ticks, ticks)

        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.tight_layout()

        f = BytesIO()
        plt.savefig(f, format = 'png')
        
        return f.getvalue()