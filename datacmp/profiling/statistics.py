"""
Statistical analysis utilities.
"""

import pandas as pd
import numpy as np
from typing import Dict, Any

from ..utils.logger import get_logger

logger = get_logger(__name__)


def compute_statistics(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Compute comprehensive statistics for DataFrame.
    
    Args:
        df: Input DataFrame
    
    Returns:
        Dictionary containing statistical measures
    
    Example:
        >>> stats = compute_statistics(df)
    """
    stats = {
        "numeric": {},
        "categorical": {},
        "overall": {}
    }
    
    # Numeric statistics
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    for col in numeric_cols:
        stats["numeric"][col] = {
            "count": int(df[col].count()),
            "mean": float(df[col].mean()),
            "median": float(df[col].median()),
            "std": float(df[col].std()),
            "min": float(df[col].min()),
            "max": float(df[col].max()),
            "q25": float(df[col].quantile(0.25)),
            "q75": float(df[col].quantile(0.75)),
            "skewness": float(df[col].skew()),
            "kurtosis": float(df[col].kurtosis()),
        }
    
    # Categorical statistics
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    
    for col in categorical_cols:
        value_counts = df[col].value_counts()
        stats["categorical"][col] = {
            "count": int(df[col].count()),
            "unique": int(df[col].nunique()),
            "top": str(value_counts.index[0]) if len(value_counts) > 0 else None,
            "freq": int(value_counts.iloc[0]) if len(value_counts) > 0 else 0,
        }
    
    # Overall statistics
    stats["overall"] = {
        "total_rows": int(len(df)),
        "total_columns": int(len(df.columns)),
        "total_missing": int(df.isnull().sum().sum()),
        "missing_percentage": float(df.isnull().sum().sum() / (len(df) * len(df.columns)) * 100),
        "duplicate_rows": int(df.duplicated().sum()),
    }
    
    return stats