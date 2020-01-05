from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

from .helper import Helper

class Distplot:
    def validate (dataframe, x_axis):
        if x_axis not in dataframe.columns:
            err = "Column {} does not exist in dataset.".format(x_axis)
            return err

        return None

    def make(dataframe, x_axis, bucket):
        series = dataframe[x_axis]
        
        if bucket == None:
            bucket = Helper.get_bucket_size(series)
        bin_edges = Helper.get_bin_edges(series, bucket)

        sb.distplot(series, bins = bin_edges, rug = True, rug_kws = {'color' : 'r'})

        # xticks = Distplot._get_x_ticks(series, bucket)
        # plt.xticks(xticks, xticks)

        plt.ylabel("KDE")
        plt.tight_layout()

        f = BytesIO()
        plt.savefig(f, format = 'png')
        
        return f.getvalue()

    def _get_x_ticks(series, bucket_size):
        min = series.min()
        max = series.max() + bucket_size
        return np.arange(min, max, bucket_size)