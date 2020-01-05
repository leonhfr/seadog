from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sb

from .helper import Helper

class Box:
    def validate(dataframe, x_axis, y_axis):
        if x_axis not in dataframe.columns:
            err = "Column '{}' does not exist in dataset.".format(x_axis)
            return err

        
        if y_axis not in dataframe.columns:
            err = "Column '{}' does not exist in dataset.".format(y_axis)
            return err

        return None

    def make(dataframe, x_axis, y_axis):
        base_color = sb.color_palette()[0]
        sb.boxplot(data = dataframe, x = x_axis, y = y_axis,
            color = base_color)
        plt.tight_layout()

        f = BytesIO()
        plt.savefig(f, format = 'png')
        
        return f.getvalue()