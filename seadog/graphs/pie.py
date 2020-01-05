from io import BytesIO
import matplotlib.pyplot as plt

from .helper import Helper

class Pie:
    def validate(dataframe, variable):
        if variable not in dataframe.columns:
            err = "Variable {} does not exist in dataset.".format(variable)
            return err

        return None

    def make(dataframe, variable):
        sorted_counts = dataframe[variable].value_counts()

        plt.pie(sorted_counts, labels = sorted_counts.index,
                startangle = 90, counterclock = False)
        plt.axis('square')
        plt.tight_layout()

        f = BytesIO()
        plt.savefig(f, format = 'png')
        
        return f.getvalue()