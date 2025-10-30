"""
Report generation utilities.
"""

import logging
from pathlib import Path
from typing import Dict, Any, List
import pandas as pd
from datetime import datetime

from ..utils.logger import get_logger

logger = get_logger(__name__)


def generate_html_report(
    df: pd.DataFrame,
    original_df: pd.DataFrame,
    profile_data: Dict[str, Any],
    cleaning_log: List[str],
    output_path: Path,
    include_plots: bool = True
) -> None:
    """
    Generate comprehensive HTML report.
    
    Args:
        df: Cleaned DataFrame
        original_df: Original DataFrame
        profile_data: Profiling information
        cleaning_log: List of cleaning operations
        output_path: Output file path
        include_plots: Whether to include visualizations
    """
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Datacmp Analysis Report</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            font-weight: 700;
        }}
        
        .header p {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        
        .content {{
            padding: 40px;
        }}
        
        .section {{
            margin-bottom: 40px;
        }}
        
        .section-title {{
            font-size: 1.8em;
            color: #667eea;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
            font-weight: 600;
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .stat-card {{
            background: #f8f9fa;
            padding: 25px;
            border-radius: 8px;
            border-left: 4px solid #667eea;
            transition: transform 0.2s;
        }}
        
        .stat-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }}
        
        .stat-label {{
            font-size: 0.9em;
            color: #666;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 8px;
        }}
        
        .stat-value {{
            font-size: 2em;
            font-weight: 700;
            color: #333;
        }}
        
        .log-item {{
            background: #f8f9fa;
            padding: 12px 20px;
            margin-bottom: 10px;
            border-left: 4px solid #28a745;
            border-radius: 4px;
        }}
        
        .log-item::before {{
            content: "✓ ";
            color: #28a745;
            font-weight: bold;
            margin-right: 8px;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 0.9em;
        }}
        
        th {{
            background: #667eea;
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: 600;
        }}
        
        td {{
            padding: 12px;
            border-bottom: 1px solid #ddd;
        }}
        
        tr:hover {{
            background: #f8f9fa;
        }}
        
        .plot-container {{
            margin: 30px 0;
            text-align: center;
        }}
        
        .plot-container img {{
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
            font-size: 0.9em;
        }}
        
        .badge {{
            display: inline-block;
            padding: 4px 12px;
            background: #667eea;
            color: white;
            border-radius: 12px;
            font-size: 0.85em;
            font-weight: 600;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Datacmp Analysis Report</h1>
            <p>Generated on {datetime.now().strftime("%B %d, %Y at %H:%M:%S")}</p>
        </div>
        
        <div class="content">
            <div class="section">
                <h2 class="section-title">Dataset Overview</h2>
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-label">Original Rows</div>
                        <div class="stat-value">{original_df.shape[0]:,}</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-label">Final Rows</div>
                        <div class="stat-value">{df.shape[0]:,}</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-label">Total Columns</div>
                        <div class="stat-value">{df.shape[1]}</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-label">Cleaning Steps</div>
                        <div class="stat-value">{len(cleaning_log)}</div>
                    </div>
                </div>
            </div>
            
            <div class="section">
                <h2 class="section-title">Cleaning Operations</h2>
                {_generate_cleaning_log_html(cleaning_log)}
            </div>
            
            <div class="section">
                <h2 class="section-title">Data Profile</h2>
                {_generate_profile_html(profile_data)}
            </div>
            
            {_generate_plots_html(profile_data) if include_plots else ''}
        </div>
        
        <div class="footer">
            <p>Generated by <strong>Datacmp v3.0</strong> | Created by Moustafa Mohamed</p>
            <p>GitHub: <a href="https://github.com/MoustafaMohamed01/datacmp">datacmp</a></p>
        </div>
    </div>
</body>
</html>
"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    logger.info(f"HTML report saved to {output_path}")


def _generate_cleaning_log_html(cleaning_log: List[str]) -> str:
    """Generate HTML for cleaning log."""
    if not cleaning_log:
        return "<p>No cleaning operations performed.</p>"
    
    html = ""
    for log_entry in cleaning_log:
        html += f'<div class="log-item">{log_entry}</div>\n'
    
    return html


def _generate_profile_html(profile_data: Dict[str, Any]) -> str:
    """Generate HTML for profile data."""
    html = ""
    
    if "summary" in profile_data:
        html += f'<pre style="background: #f8f9fa; padding: 20px; border-radius: 8px; overflow-x: auto;">{profile_data["summary"]}</pre>'
    
    return html


def _generate_plots_html(profile_data: Dict[str, Any]) -> str:
    """Generate HTML for plots section."""
    if "plots" not in profile_data or not profile_data["plots"]:
        return ""
    
    html = '<div class="section"><h2 class="section-title">Visualizations</h2>'
    
    plots = profile_data["plots"]
    
    if "missing_heatmap" in plots:
        html += '''
        <div class="plot-container">
            <h3>Missing Values Heatmap</h3>
            <img src="missing_heatmap.png" alt="Missing Values Heatmap">
        </div>
        '''
    
    if "correlation_heatmap" in plots:
        html += '''
        <div class="plot-container">
            <h3>Correlation Heatmap</h3>
            <img src="correlation_heatmap.png" alt="Correlation Heatmap">
        </div>
        '''
    
    if "distributions" in plots:
        html += '''
        <div class="plot-container">
            <h3>Feature Distributions</h3>
            <img src="distributions.png" alt="Feature Distributions">
        </div>
        '''
    
    html += '</div>'
    
    return html


def generate_txt_report(
    df: pd.DataFrame,
    original_df: pd.DataFrame,
    profile_data: Dict[str, Any],
    cleaning_log: List[str],
    output_path: Path
) -> None:
    """
    Generate text report.
    
    Args:
        df: Cleaned DataFrame
        original_df: Original DataFrame
        profile_data: Profiling information
        cleaning_log: List of cleaning operations
        output_path: Output file path
    """
    report = f"""
{'='*80}
DATACMP ANALYSIS REPORT
{'='*80}

Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

{'='*80}
DATASET OVERVIEW
{'='*80}

Original Shape: {original_df.shape[0]} rows × {original_df.shape[1]} columns
Final Shape:    {df.shape[0]} rows × {df.shape[1]} columns
Rows Removed:   {original_df.shape[0] - df.shape[0]}

{'='*80}
CLEANING OPERATIONS
{'='*80}

"""
    
    if cleaning_log:
        for i, log_entry in enumerate(cleaning_log, 1):
            report += f"{i}. {log_entry}\n"
    else:
        report += "No cleaning operations performed.\n"
    
    report += f"\n{'='*80}\n"
    report += "DATA PROFILE\n"
    report += f"{'='*80}\n\n"
    
    if "summary" in profile_data:
        report += profile_data["summary"]
    
    report += f"\n\n{'='*80}\n"
    report += "Generated by Datacmp v3.0\n"
    report += "Author: Moustafa Mohamed\n"
    report += "GitHub: https://github.com/MoustafaMohamed01/datacmp\n"
    report += f"{'='*80}\n"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    logger.info(f"Text report saved to {output_path}")