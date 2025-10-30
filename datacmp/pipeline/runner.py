"""
Pipeline execution utilities.
"""

import logging
from pathlib import Path
from typing import Optional, Union
import pandas as pd

from .config import load_config
from ..core.datacmp import DataCmp
from ..utils.logger import get_logger

logger = get_logger(__name__)


def run_pipeline(
    data: Union[str, Path, pd.DataFrame],
    config_path: Optional[Union[str, Path]] = None,
    export_csv_path: Optional[Union[str, Path]] = None,
    export_report_path: Optional[Union[str, Path]] = None,
    verbose: bool = True
) -> pd.DataFrame:
    """
    Run complete data cleaning and profiling pipeline.
    
    Args:
        data: Path to CSV file or pandas DataFrame
        config_path: Path to YAML configuration file
        export_csv_path: Path to save cleaned CSV
        export_report_path: Path to save report
        verbose: Print progress messages
    
    Returns:
        Cleaned pandas DataFrame
    
    Example:
        >>> df_clean = run_pipeline("data.csv", config_path="config.yaml")
    """
    if verbose:
        print("\n" + "="*80)
        print("DATACMP PIPELINE")
        print("="*80 + "\n")
    
    # Initialize DataCmp
    cmp = DataCmp(data, config=config_path)
    
    if verbose:
        print(f"[1/4] Loaded data: {cmp.df.shape[0]} rows × {cmp.df.shape[1]} columns")
    
    # Clean data
    if verbose:
        print("[2/4] Cleaning data...")
    cmp.clean()
    
    # Profile data
    if verbose:
        print("[3/4] Generating profile...")
    cmp.profile()
    
    # Export results
    if verbose:
        print("[4/4] Exporting results...")
    
    if export_csv_path:
        cmp.export(export_csv_path, format="csv")
    
    if export_report_path:
        report_path = Path(export_report_path)
        format_type = report_path.suffix.lstrip('.')
        cmp.export(export_report_path, format=format_type)
    
    if verbose:
        print("\n" + "="*80)
        print("PIPELINE COMPLETE")
        print("="*80 + "\n")
        print(f"Final shape: {cmp.df.shape[0]} rows × {cmp.df.shape[1]} columns")
        print(f"Cleaning operations: {len(cmp.cleaning_log)}")
    
    return cmp.df