"""
Missing value handling utilities.
"""

import logging
from typing import Tuple, List, Dict, Any
import pandas as pd

from ..utils.logger import get_logger

logger = get_logger(__name__)


def handle_missing_values(
    df: pd.DataFrame,
    config: Dict[str, Any]
) -> Tuple[pd.DataFrame, List[str]]:
    """
    Handle missing values based on configuration.
    
    Args:
        df: Input DataFrame
        config: Cleaning configuration
    
    Returns:
        Tuple of (cleaned DataFrame, list of log messages)
    
    Example:
        >>> df, log = handle_missing_values(df, config)
    """
    df = df.copy()
    log = []
    
    threshold_drop = config.get("threshold_drop", 0.45)
    fill_strategy = config.get("fill_strategy", {})
    
    # Calculate missing ratios
    missing_info = df.isnull().mean()
    
    # Drop columns exceeding threshold
    for col in df.columns:
        missing_ratio = missing_info[col]
        
        if missing_ratio > threshold_drop:
            df.drop(columns=[col], inplace=True)
            msg = f"Dropped column '{col}' ({missing_ratio:.1%} missing)"
            logger.warning(msg)
            log.append(msg)
            continue
        
        # Fill remaining missing values
        if missing_ratio > 0:
            if pd.api.types.is_numeric_dtype(df[col]):
                strategy = fill_strategy.get("numeric", "median")
                df, fill_msg = _fill_numeric(df, col, strategy)
                log.append(fill_msg)
            else:
                strategy = fill_strategy.get("categorical", "mode")
                df, fill_msg = _fill_categorical(df, col, strategy)
                log.append(fill_msg)
    
    return df, log


def _fill_numeric(
    df: pd.DataFrame,
    col: str,
    strategy: str
) -> Tuple[pd.DataFrame, str]:
    """Fill missing values in numeric column."""
    if strategy == "mean":
        fill_value = df[col].mean()
    elif strategy == "median":
        fill_value = df[col].median()
    elif strategy == "mode":
        mode = df[col].mode()
        fill_value = mode[0] if not mode.empty else 0
    else:
        fill_value = df[col].median()
    
    df[col] = df[col].fillna(fill_value)
    msg = f"Filled numeric column '{col}' with {strategy} ({fill_value:.2f})"
    logger.info(msg)
    
    return df, msg


def _fill_categorical(
    df: pd.DataFrame,
    col: str,
    strategy: str
) -> Tuple[pd.DataFrame, str]:
    """Fill missing values in categorical column."""
    if strategy == "mode":
        mode = df[col].mode()
        fill_value = mode[0] if not mode.empty else "Unknown"
    else:
        fill_value = "Unknown"
    
    df[col] = df[col].fillna(fill_value)
    msg = f"Filled categorical column '{col}' with '{fill_value}'"
    logger.info(msg)
    
    return df, msg