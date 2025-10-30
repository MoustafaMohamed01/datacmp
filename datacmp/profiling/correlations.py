"""
Correlation analysis utilities.
"""

import pandas as pd
import numpy as np
from typing import Dict, Optional

from ..utils.logger import get_logger

logger = get_logger(__name__)


def compute_correlations(
    df: pd.DataFrame,
    method: str = "pearson"
) -> Optional[pd.DataFrame]:
    """
    Compute correlation matrix for numeric columns.
    
    Args:
        df: Input DataFrame
        method: Correlation method ('pearson', 'spearman', 'kendall')
    
    Returns:
        Correlation matrix or None if insufficient numeric columns
    
    Example:
        >>> corr_matrix = compute_correlations(df, method='spearman')
    """
    numeric_df = df.select_dtypes(include=[np.number])
    
    if numeric_df.shape[1] < 2:
        logger.warning("Insufficient numeric columns for correlation analysis")
        return None
    
    try:
        corr_matrix = numeric_df.corr(method=method)
        logger.info(f"Computed {method} correlation matrix")
        return corr_matrix
    except Exception as e:
        logger.error(f"Error computing correlations: {e}")
        return None