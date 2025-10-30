"""
Main DataCmp class - The primary interface for datacmp functionality.
"""

import logging
from pathlib import Path
from typing import Optional, Union, Dict, Any, List
import pandas as pd

from ..cleaning.columns import clean_column_names
from ..cleaning.missing import handle_missing_values
from ..cleaning.outliers import handle_outliers
from ..profiling.summary import generate_summary
from ..profiling.statistics import compute_statistics
from ..profiling.correlations import compute_correlations
from ..visuals.plots import create_visualizations
from ..visuals.reports import generate_html_report, generate_txt_report
from ..pipeline.config import load_config
from ..utils.logger import get_logger

logger = get_logger(__name__)


class DataCmp:
    """
    DataCmp: A powerful class for data cleaning and exploratory data analysis.
    
    Example:
        >>> from datacmp import DataCmp
        >>> cmp = DataCmp("data.csv")
        >>> cmp.clean().profile().export("report.html")
    
    Attributes:
        df (pd.DataFrame): The working DataFrame
        original_df (pd.DataFrame): The original DataFrame (backup)
        config (dict): Configuration settings
        cleaning_log (list): Log of cleaning operations
    """
    
    def __init__(
        self,
        data: Union[str, Path, pd.DataFrame],
        config: Optional[Union[str, Path, Dict]] = None,
        auto_clean: bool = False
    ):
        """
        Initialize DataCmp instance.
        
        Args:
            data: Path to CSV file or pandas DataFrame
            config: Path to YAML config file or config dictionary
            auto_clean: If True, automatically run basic cleaning
        
        Example:
            >>> cmp = DataCmp("data.csv")
            >>> cmp = DataCmp(df, config="config.yaml")
        """
        logger.info("Initializing DataCmp...")
        
        # Load data
        if isinstance(data, (str, Path)):
            self.df = pd.read_csv(data)
            logger.info(f"Loaded data from {data}: {self.df.shape[0]} rows, {self.df.shape[1]} columns")
        elif isinstance(data, pd.DataFrame):
            self.df = data.copy()
            logger.info(f"Loaded DataFrame: {self.df.shape[0]} rows, {self.df.shape[1]} columns")
        else:
            raise TypeError("data must be a file path or pandas DataFrame")
        
        # Store original
        self.original_df = self.df.copy()
        
        # Load configuration
        if config is None:
            self.config = self._default_config()
        elif isinstance(config, (str, Path)):
            self.config = load_config(config)
        elif isinstance(config, dict):
            self.config = config
        else:
            raise TypeError("config must be a file path or dictionary")
        
        # Initialize tracking
        self.cleaning_log: List[str] = []
        self._profile_cache: Dict[str, Any] = {}
        
        # Auto-clean if requested
        if auto_clean:
            self.clean()
    
    def _default_config(self) -> Dict[str, Any]:
        """Return default configuration."""
        return {
            "cleaning": {
                "threshold_drop": 0.45,
                "fill_strategy": {
                    "numeric": "median",
                    "categorical": "mode"
                },
                "outlier_handling": {
                    "enabled": True,
                    "method": "iqr",
                    "iqr_multiplier": 1.5,
                    "action": "cap"
                }
            },
            "drop_duplicates": True,
            "profiling": {
                "include_more_stats": True,
                "compute_correlations": True
            }
        }
    
    def clean(
        self,
        columns: bool = True,
        missing: bool = True,
        outliers: bool = True,
        duplicates: bool = True
    ) -> "DataCmp":
        """
        Clean the dataset using various strategies.
        
        Args:
            columns: Clean column names
            missing: Handle missing values
            outliers: Handle outliers
            duplicates: Remove duplicates
        
        Returns:
            self for method chaining
        
        Example:
            >>> cmp.clean(outliers=False)
        """
        logger.info("Starting data cleaning...")
        
        if columns:
            self.df, log = clean_column_names(self.df)
            self.cleaning_log.extend(log)
        
        if duplicates and self.config.get("drop_duplicates", True):
            initial_rows = len(self.df)
            self.df = self.df.drop_duplicates()
            dropped = initial_rows - len(self.df)
            if dropped > 0:
                msg = f"Removed {dropped} duplicate rows"
                logger.info(msg)
                self.cleaning_log.append(msg)
        
        if missing:
            self.df, log = handle_missing_values(
                self.df,
                self.config.get("cleaning", {})
            )
            self.cleaning_log.extend(log)
        
        if outliers and self.config.get("cleaning", {}).get("outlier_handling", {}).get("enabled", False):
            self.df, log = handle_outliers(
                self.df,
                self.config.get("cleaning", {}).get("outlier_handling", {})
            )
            self.cleaning_log.extend(log)
        
        logger.info(f"Cleaning complete. Final shape: {self.df.shape}")
        return self
    
    def profile(self, detailed: bool = True) -> "DataCmp":
        """
        Generate profiling information for the dataset.
        
        Args:
            detailed: Include extended statistics
        
        Returns:
            self for method chaining
        
        Example:
            >>> cmp.profile()
        """
        logger.info("Generating data profile...")
        
        self._profile_cache["summary"] = generate_summary(
            self.df,
            self.config.get("profiling", {})
        )
        
        if detailed:
            self._profile_cache["statistics"] = compute_statistics(self.df)
            
            if self.config.get("profiling", {}).get("compute_correlations", True):
                self._profile_cache["correlations"] = compute_correlations(self.df)
        
        logger.info("Profiling complete")
        return self
    
    def visualize(self, output_dir: Optional[Union[str, Path]] = None) -> "DataCmp":
        """
        Create visualizations for the dataset.
        
        Args:
            output_dir: Directory to save plots (optional)
        
        Returns:
            self for method chaining
        
        Example:
            >>> cmp.visualize("./plots")
        """
        logger.info("Creating visualizations...")
        
        plots = create_visualizations(
            self.df,
            output_dir=output_dir,
            show_plots=output_dir is None
        )
        
        self._profile_cache["plots"] = plots
        logger.info(f"Created {len(plots)} visualizations")
        return self
    
    def export(
        self,
        output: Union[str, Path],
        format: Optional[str] = None,
        include_plots: bool = True
    ) -> "DataCmp":
        """
        Export cleaned data and/or reports.
        
        Args:
            output: Output file path
            format: Export format ('csv', 'html', 'txt'). Auto-detected from extension if None
            include_plots: Include visualizations in reports
        
        Returns:
            self for method chaining
        
        Example:
            >>> cmp.export("cleaned_data.csv")
            >>> cmp.export("report.html")
        """
        output_path = Path(output)
        
        if format is None:
            format = output_path.suffix.lstrip('.')
        
        format = format.lower()
        
        if format == "csv":
            self.df.to_csv(output_path, index=False)
            logger.info(f"Exported cleaned data to {output_path}")
        
        elif format == "html":
            # Ensure we have profiling data
            if not self._profile_cache:
                self.profile()
            
            generate_html_report(
                self.df,
                self.original_df,
                self._profile_cache,
                self.cleaning_log,
                output_path,
                include_plots=include_plots
            )
            logger.info(f"Generated HTML report: {output_path}")
        
        elif format == "txt":
            if not self._profile_cache:
                self.profile()
            
            generate_txt_report(
                self.df,
                self.original_df,
                self._profile_cache,
                self.cleaning_log,
                output_path
            )
            logger.info(f"Generated text report: {output_path}")
        
        else:
            raise ValueError(f"Unsupported format: {format}")
        
        return self
    
    def reset(self) -> "DataCmp":
        """
        Reset to original DataFrame.
        
        Returns:
            self for method chaining
        """
        self.df = self.original_df.copy()
        self.cleaning_log = []
        self._profile_cache = {}
        logger.info("Reset to original DataFrame")
        return self
    
    def get_summary(self) -> str:
        """Get dataset summary as string."""
        if "summary" not in self._profile_cache:
            self._profile_cache["summary"] = generate_summary(
                self.df,
                self.config.get("profiling", {})
            )
        return self._profile_cache["summary"]
    
    def get_cleaning_log(self) -> List[str]:
        """Get list of cleaning operations performed."""
        return self.cleaning_log.copy()
    
    def __repr__(self) -> str:
        return f"DataCmp(shape={self.df.shape}, cleaned={len(self.cleaning_log) > 0})"
    
    def __str__(self) -> str:
        return self.get_summary()