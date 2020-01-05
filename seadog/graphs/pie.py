from io import BytesIO
import matplotlib.pyplot as plt

from .helper import Helper

class Pie:
    def validate(dataframe, column):
        if column not in dataframe.columns:
            err = "Column '{}' does not exist in dataset.".format(column)
            return err

        return None

    def make(dataframe, column):
        sorted_counts = dataframe[column].value_counts()

        plt.pie(sorted_counts, labels = sorted_counts.index,
                startangle = 90, counterclock = False)
        plt.axis('square')
        plt.tight_layout()

        f = BytesIO()
        plt.savefig(f, format = 'png')
        
        return f.getvalue()