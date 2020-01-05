from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np

from .helper import Helper

class Histogram:
    def make(dataframe, x_axis, bucket, log, discrete):
        if x_axis not in dataframe.columns:
            err = "Column {} does not exist in dataset.".format(x_axis)
            ctx.fail(err)

        series = dataframe[x_axis]
        
        if bucket == None:
            bucket = Helper.get_bucket_size(series)
        bin_edges = Helper.get_bin_edges(series, bucket)

        width = 1.0
        if discrete:
            width = 0.7

        plt.hist(data = dataframe, x = x_axis, bins = bin_edges, rwidth = width)

        xticks = Histogram._get_x_ticks(series, bucket)
        plt.xticks(xticks, xticks)

        if log:
            max = plt.ylim()[1]
            ticks = Helper.get_log_ticks(max)
            plt.yscale('log')
            plt.yticks(ticks, ticks)

        f = BytesIO()
        plt.savefig(f, format = 'png')
        
        return f.getvalue()

    def _get_x_ticks(series, bucket_size):
        min = series.min()
        max = series.max() + bucket_size
        return np.arange(min, max, bucket_size)