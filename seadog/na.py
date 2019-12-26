import termplotlib as tpl

class Na:
    def get_na(dataframe, total):
        na_count = dataframe.isnull().sum().sum()

        if (na_count == 0):
            return 'This dataset has no missing data.'
        
        na_counts = dataframe.isna().sum()
        na_values = na_counts.values.tolist()
        na_labels = na_counts.index.values.tolist()

        if (total == True):
            na_values.append(dataframe.index.size)
            na_labels.append('TOTAL ELEMENTS')
        
        fig = tpl.figure()
        fig.barh(na_values,
                 na_labels,
                 force_ascii = True)

        return fig.get_string()

    def remove_na(dataframe, remove_rows, remove_cols):
        output = dataframe.copy()
        if remove_rows == True:
            output.dropna(axis = 0, inplace = True)
        if remove_cols == True:
            output.dropna(axis = 1, inplace = True)
        return output

    def get_diff(df1, df2):
        df1_cols = df1.columns.size
        df2_cols = df2.columns.size
        dif_cols = df1_cols - df2_cols

        df1_rows = df1.index.size
        df2_rows = df2.index.size
        dif_rows = df1_rows - df2_rows

        diff = str.format("This will remove {} columns and {} rows.", 
                          dif_cols, dif_rows)

        return diff