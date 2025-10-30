"""
Utility helper functions.
"""

import pandas as pd
from typing import List, Tuple


def identify_column_types(df: pd.DataFrame) -> Tuple[List[str], List[str], List[str]]:
    """
    Identify numeric, categorical, and datetime columns.
    
    Args:
        df: Input DataFrame
    
    Returns:
        Tuple of (numeric_cols, categorical_cols, datetime_cols)
    """
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    datetime_cols = df.select_dtypes(include=['datetime']).columns.tolist()
    
    return numeric_cols, categorical_cols, datetime_cols


def memory_usage_mb(df: pd.DataFrame) -> float:
    """
    Calculate DataFrame memory usage in MB.
    
    Args:
        df: Input DataFrame
    
    Returns:
        Memory usage in megabytes
    """
    return df.memory_usage(deep=True).sum() / (1024 ** 2)