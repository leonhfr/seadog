from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sb

from .helper import Helper

class Barchart:
    def make(dataframe, x_axis, log):
        if x_axis not in dataframe.columns:
            err = "Column {} does not exist in dataset.".format(x_axis)
            ctx.fail(err)
        
        base_color = sb.color_palette()[0]
        cat_order = dataframe[x_axis].value_counts().index
        sb.countplot(data = dataframe, x = x_axis, color = base_color, order = cat_order)
        plt.xticks(rotation = 90)

        if log:
            max = plt.ylim()[1]
            ticks = Helper.get_log_ticks(max)
            plt.yscale('log')
            plt.yticks(ticks, ticks)

        plt.tight_layout()

        f = BytesIO()
        plt.savefig(f, format = 'png')
        
        return f.getvalue()