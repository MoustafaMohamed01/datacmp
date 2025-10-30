"""
Dataset summary generation.
"""

import pandas as pd
from typing import Dict, Any
from tabulate import tabulate

from ..utils.logger import get_logger

logger = get_logger(__name__)


def generate_summary(df: pd.DataFrame, config: Dict[str, Any]) -> str:
    """
    Generate comprehensive dataset summary.
    
    Args:
        df: Input DataFrame
        config: Profiling configuration
    
    Returns:
        Formatted string summary
    
    Example:
        >>> summary = generate_summary(df, config)
        >>> print(summary)
    """
    num_rows, num_cols = df.shape
    
    include_more_stats = config.get("include_more_stats", True)
    
    # Column type counts
    numeric, categorical, datetime, other = _count_column_types(df)
    
    # Overview table
    overview_data = [
        ["Total Rows", num_rows],
        ["Total Columns", num_cols],
        ["Numeric Columns", numeric],
        ["Categorical Columns", categorical],
        ["Datetime Columns", datetime],
        ["Other Types", other],
        ["Memory Usage", f"{df.memory_usage(deep=True).sum() / 1024**2:.2f} MB"]
    ]
    
    overview_table = tabulate(
        overview_data,
        headers=["Metric", "Value"],
        tablefmt="rounded_outline"
    )
    
    # Column details
    headers = ["Column", "Type", "Null", "Not Null", "Null %", "Unique"]
    
    if include_more_stats:
        headers.extend(["Mean", "Median", "Std", "Skew", "Kurt"])
    
    data = []
    null_counts = df.isnull().sum()
    total_counts = df.count()
    
    for col in df.columns:
        dtype = df[col].dtype
        null = null_counts[col]
        not_null = total_counts[col]
        null_percent = f"{null / num_rows:.1%}" if num_rows > 0 else "0%"
        unique = df[col].nunique()
        
        row = [col, dtype, null, not_null, null_percent, unique]
        
        if include_more_stats:
            if pd.api.types.is_numeric_dtype(dtype):
                row.extend([
                    f"{df[col].mean():.2f}",
                    f"{df[col].median():.2f}",
                    f"{df[col].std():.2f}",
                    f"{df[col].skew():.2f}",
                    f"{df[col].kurtosis():.2f}"
                ])
            else:
                row.extend(["-", "-", "-", "-", "-"])
        
        data.append(row)
    
    details_table = tabulate(
        data,
        headers=headers,
        tablefmt="rounded_outline"
    )
    
    return f"{overview_table}\n\n{details_table}"


def _count_column_types(df: pd.DataFrame) -> tuple:
    """Count columns by type."""
    numeric = df.select_dtypes(include=['number']).shape[1]
    categorical = df.select_dtypes(include=['object', 'category']).shape[1]
    datetime = df.select_dtypes(include=['datetime']).shape[1]
    other = df.shape[1] - (numeric + categorical + datetime)
    
    return numeric, categorical, datetime, other