from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

from .helper import Helper

class Scatterplot:
    def validate(dataframe, x_axis, y_axis):
        if x_axis not in dataframe.columns:
            err = "Column '{}' does not exist in dataset.".format(x_axis)
            return err

        
        if y_axis not in dataframe.columns:
            err = "Column '{}' does not exist in dataset.".format(y_axis)
            return err

        return None

    def make(dataframe, x_axis, y_axis, xlog, ylog, regline, size):
        figsize = Helper.get_figsize(size)
        plt.figure(figsize = figsize)

        x_label = x_axis
        y_label = y_axis
        x_data = dataframe[x_axis].apply(Helper.log_trans, apply = xlog)
        y_data = dataframe[y_axis].apply(Helper.log_trans, apply = ylog)

        sb.regplot(x_data, y_data, fit_reg = regline)

        if xlog:
            x_label = 'log(' + x_label + ')'
            max = dataframe[x_axis].max()
            ticks = Helper.get_log_ticks(max)
            plt.xticks(Helper.log_trans(ticks), ticks)

        if ylog:
            y_label = 'log(' + y_label + ')'
            max = dataframe[y_axis].max()
            ticks = Helper.get_log_ticks(max)
            plt.yticks(Helper.log_trans(ticks), ticks)

        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.tight_layout()

        f = BytesIO()
        plt.savefig(f, format = 'png')
        
        return f.getvalue()
