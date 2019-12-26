from tabulate import tabulate

class Stats:
    def get_description(dataframe):
        description = dataframe.describe()
        table = Stats._make_table(description)
        return table

    def get_sample(dataframe, n):
        sample = dataframe.sample(n)
        table = Stats._make_table(sample)
        return table

    def get_correlation(dataframe):
        correlation = dataframe.corr()
        table = Stats._make_table(correlation)
        return table

    def _make_table(dataframe):
        return tabulate(dataframe,
                        headers = dataframe.columns,
                        numalign = 'right')

