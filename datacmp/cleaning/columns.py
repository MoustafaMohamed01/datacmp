"""
Column name cleaning utilities.
"""

import logging
from typing import Tuple, List
import pandas as pd

from ..utils.logger import get_logger

logger = get_logger(__name__)


def clean_column_names(df: pd.DataFrame) -> Tuple[pd.DataFrame, List[str]]:
    """
    Clean and standardize DataFrame column names.
    
    Operations:
    - Strip whitespace
    - Convert to lowercase
    - Replace spaces with underscores
    - Remove special characters
    
    Args:
        df: Input DataFrame
    
    Returns:
        Tuple of (cleaned DataFrame, list of log messages)
    
    Example:
        >>> df, log = clean_column_names(df)
    """
    df = df.copy()
    original_columns = df.columns.tolist()
    log = []
    
    # Clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('[^a-z0-9_]', '', regex=True)
    )
    
    cleaned_columns = df.columns.tolist()
    
    # Log changes
    for orig, cleaned in zip(original_columns, cleaned_columns):
        if orig != cleaned:
            msg = f"Renamed column: '{orig}' → '{cleaned}'"
            logger.info(msg)
            log.append(msg)
    
    return df, log