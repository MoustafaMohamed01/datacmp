"""
Visualization generation utilities.
"""

import logging
from pathlib import Path
from typing import Optional, Dict, Any, List
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from ..utils.logger import get_logger

logger = get_logger(__name__)

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)


def create_visualizations(
    df: pd.DataFrame,
    output_dir: Optional[Path] = None,
    show_plots: bool = False
) -> Dict[str, Any]:
    """
    Create comprehensive visualizations for the dataset.
    
    Args:
        df: Input DataFrame
        output_dir: Directory to save plots
        show_plots: Whether to display plots
    
    Returns:
        Dictionary of plot information
    
    Example:
        >>> plots = create_visualizations(df, output_dir="./plots")
    """
    plots = {}
    
    if output_dir:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
    
    # Missing values heatmap
    if df.isnull().sum().sum() > 0:
        plots['missing_heatmap'] = _plot_missing_heatmap(
            df, output_dir, show_plots
        )
    
    # Correlation heatmap
    numeric_df = df.select_dtypes(include=[np.number])
    if numeric_df.shape[1] >= 2:
        plots['correlation_heatmap'] = _plot_correlation_heatmap(
            numeric_df, output_dir, show_plots
        )
    
    # Distribution plots for numeric columns
    if numeric_df.shape[1] > 0:
        plots['distributions'] = _plot_distributions(
            numeric_df, output_dir, show_plots
        )
    
    logger.info(f"Created {len(plots)} visualizations")
    return plots


def _plot_missing_heatmap(
    df: pd.DataFrame,
    output_dir: Optional[Path],
    show: bool
) -> str:
    """Create missing values heatmap."""
    plt.figure(figsize=(12, 8))
    
    missing_matrix = df.isnull()
    
    sns.heatmap(
        missing_matrix,
        cbar=True,
        cmap='viridis',
        yticklabels=False
    )
    
    plt.title('Missing Values Heatmap', fontsize=16, fontweight='bold')
    plt.xlabel('Columns')
    plt.ylabel('Rows')
    plt.tight_layout()
    
    if output_dir:
        path = output_dir / "missing_heatmap.png"
        plt.savefig(path, dpi=300, bbox_inches='tight')
        logger.info(f"Saved missing heatmap to {path}")
    
    if show:
        plt.show()
    else:
        plt.close()
    
    return "missing_heatmap.png"


def _plot_correlation_heatmap(
    df: pd.DataFrame,
    output_dir: Optional[Path],
    show: bool
) -> str:
    """Create correlation heatmap."""
    plt.figure(figsize=(12, 10))
    
    corr_matrix = df.corr()
    
    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt='.2f',
        cmap='coolwarm',
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.8}
    )
    
    plt.title('Correlation Heatmap', fontsize=16, fontweight='bold')
    plt.tight_layout()
    
    if output_dir:
        path = output_dir / "correlation_heatmap.png"
        plt.savefig(path, dpi=300, bbox_inches='tight')
        logger.info(f"Saved correlation heatmap to {path}")
    
    if show:
        plt.show()
    else:
        plt.close()
    
    return "correlation_heatmap.png"


def _plot_distributions(
    df: pd.DataFrame,
    output_dir: Optional[Path],
    show: bool
) -> List[str]:
    """Create distribution plots for numeric columns."""
    plots = []
    
    # Limit to first 12 columns to avoid overwhelming plots
    cols_to_plot = df.columns[:12]
    
    n_cols = min(3, len(cols_to_plot))
    n_rows = (len(cols_to_plot) + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 4 * n_rows))
    
    if n_rows == 1 and n_cols == 1:
        axes = np.array([axes])
    axes = axes.flatten() if n_rows > 1 or n_cols > 1 else [axes]
    
    for idx, col in enumerate(cols_to_plot):
        ax = axes[idx]
        df[col].hist(bins=30, edgecolor='black', alpha=0.7, ax=ax)
        ax.set_title(f'Distribution of {col}', fontweight='bold')
        ax.set_xlabel(col)
        ax.set_ylabel('Frequency')
    
    # Hide unused subplots
    for idx in range(len(cols_to_plot), len(axes)):
        axes[idx].set_visible(False)
    
    plt.tight_layout()
    
    if output_dir:
        path = output_dir / "distributions.png"
        plt.savefig(path, dpi=300, bbox_inches='tight')
        logger.info(f"Saved distributions to {path}")
        plots.append("distributions.png")
    
    if show:
        plt.show()
    else:
        plt.close()
    
    return plots