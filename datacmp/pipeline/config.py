"""
Configuration management utilities.
"""

import logging
from pathlib import Path
from typing import Dict, Any, Union
import yaml

from ..utils.logger import get_logger

logger = get_logger(__name__)


def load_config(config_path: Union[str, Path]) -> Dict[str, Any]:
    """
    Load configuration from YAML file.
    
    Args:
        config_path: Path to YAML configuration file
    
    Returns:
        Configuration dictionary
    
    Example:
        >>> config = load_config("config.yaml")
    """
    config_path = Path(config_path)
    
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    logger.info(f"Loaded configuration from {config_path}")
    return config


def save_config(config: Dict[str, Any], output_path: Union[str, Path]) -> None:
    """
    Save configuration to YAML file.
    
    Args:
        config: Configuration dictionary
        output_path: Output file path
    
    Example:
        >>> save_config(config, "my_config.yaml")
    """
    output_path = Path(output_path)
    
    with open(output_path, 'w') as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False)
    
    logger.info(f"Saved configuration to {output_path}")


def get_default_config() -> Dict[str, Any]:
    """
    Get default configuration.
    
    Returns:
        Default configuration dictionary
    """
    return {
        "library_name": "datacmp",
        "version": "3.0.0",
        "author": "Moustafa Mohamed",
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