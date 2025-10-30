"""
Datacmp - A powerful Python library for data cleaning and exploratory data analysis.

Author: Moustafa Mohamed
GitHub: https://github.com/MoustafaMohamed01/datacmp
License: MIT
"""

from .core.datacmp import DataCmp
from .pipeline.runner import run_pipeline
from .pipeline.config import load_config, save_config

__version__ = "3.0.0"
__author__ = "Moustafa Mohamed"
__email__ = "moustafa.mh.mohamed@gmail.com"

__all__ = [
    "DataCmp",
    "run_pipeline",
    "load_config",
    "save_config",
]