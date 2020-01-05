from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

from .helper import Helper

class Scatterplot:
    def validate(dataframe, x_axis, y_axis):
        if x_axis not in dataframe.columns:
            err = "Column {} does not exist in dataset.".format(x_axis)
            return err

        
        if y_axis not in dataframe.columns:
            err = "Column {} does not exist in dataset.".format(y_axis)
            return err

        return None

    def make(dataframe, x_axis, y_axis, xlog, ylog, regline):
        print("hello")