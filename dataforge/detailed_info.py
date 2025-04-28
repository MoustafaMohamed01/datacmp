from tabulate import tabulate
import pandas as pd

def get_detailed(df):

    num_rows, num_cols = df.shape
    data = [
        ["Number of Rows", num_rows, "", "", ""],
        ["Number of Columns", num_cols, "", "", ""],
        ["Column Name", "Dtype", "Null", "Not Null", "Mean"],
    ]

    null_counts = df.isnull().sum()
    total_counts = df.count()

    for col in df.columns:
        dtype = df[col].dtype
        null = null_counts.get(col, 0)
        not_null = total_counts.get(col, 0)
        mean_val = df[col].mean() if pd.api.types.is_numeric_dtype(dtype) else "-"
        data.append([col, dtype, null, not_null, mean_val])

    return tabulate(data, headers="firstrow", tablefmt="grid")

