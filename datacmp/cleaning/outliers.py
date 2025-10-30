"""
Outlier detection and handling utilities.
"""

import logging
from typing import Tuple, List, Dict, Any
import pandas as pd
import numpy as np

from ..utils.logger import get_logger

logger = get_logger(__name__)


def handle_outliers(
    df: pd.DataFrame,
    config: Dict[str, Any]
) -> Tuple[pd.DataFrame, List[str]]:
    """
    Detect and handle outliers using IQR method.
    
    Args:
        df: Input DataFrame
        config: Outlier handling configuration
    
    Returns:
        Tuple of (cleaned DataFrame, list of log messages)
    
    Example:
        >>> df, log = handle_outliers(df, config)
    """
    df = df.copy()
    log = []
    
    method = config.get("method", "iqr")
    action = config.get("action", "cap")
    iqr_multiplier = config.get("iqr_multiplier", 1.5)
    
    if method != "iqr":
        logger.warning(f"Unknown outlier method: {method}. Using IQR.")
    
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    for col in numeric_cols:
        df, handled_count = _handle_outliers_iqr(
            df,
            col,
            iqr_multiplier,
            action
        )
        
        if handled_count > 0:
            msg = f"Handled {handled_count} outliers in '{col}' (action: {action})"
            logger.info(msg)
            log.append(msg)
    
    return df, log


def _handle_outliers_iqr(
    df: pd.DataFrame,
    col: str,
    multiplier: float,
    action: str
) -> Tuple[pd.DataFrame, int]:
    """
    Handle outliers in a single column using IQR method.
    
    Args:
        df: Input DataFrame
        col: Column name
        multiplier: IQR multiplier
        action: 'cap' or 'remove'
    
    Returns:
        Tuple of (DataFrame, number of outliers handled)
    """
    series = df[col]
    
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    
    lower_bound = q1 - multiplier * iqr
    upper_bound = q3 + multiplier * iqr
    
    outliers_mask = ~series.between(lower_bound, upper_bound)
    outlier_count = outliers_mask.sum()
    
    if outlier_count == 0:
        return df, 0
    
    if action == "cap":
        df[col] = series.clip(lower=lower_bound, upper=upper_bound)
    elif action == "remove":
        df = df[~outliers_mask]
    else:
        logger.warning(f"Unknown action: {action}. Using 'cap'.")
        df[col] = series.clip(lower=lower_bound, upper=upper_bound)
    
    return df, outlier_count