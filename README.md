# Datacmp

[![PyPI version](https://badge.fury.io/py/datacmp.svg)](https://pypi.org/project/datacmp/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/datacmp)](https://pepy.tech/project/datacmp)

**Datacmp** is a powerful, lightweight Python library designed to simplify and accelerate data cleaning and exploratory data analysis (EDA) workflows. Built for data scientists and analysts, it provides intelligent preprocessing, structured insights, and beautiful visualizations—all with just a few lines of code.

---

## Features

### **Smart Data Cleaning**

- **Automatic column name standardization** (lowercase, underscores, no special chars)
- **Intelligent missing value handling** with configurable strategies (mean, median, mode)
- **Outlier detection and handling** using IQR method (cap or remove)
- **Duplicate row removal** with detailed logging
- **Configurable threshold-based column dropping**

### **Comprehensive Profiling**

- **Dataset overview** with row/column counts and memory usage
- **Detailed column analysis** including dtypes, missing values, and unique counts
- **Extended statistics** (mean, median, std, skewness, kurtosis)
- **Correlation analysis** (Pearson, Spearman, Kendall)
- **Column type detection** (numeric, categorical, datetime)

### **Beautiful Visualizations**

- **Missing value heatmaps**
- **Correlation matrices**
- **Distribution plots** for numeric features
- **Export-ready plots** in high resolution

### **Flexible Reporting**

- **HTML reports** with interactive styling and embedded visualizations
- **Text reports** for quick inspection
- **CSV export** of cleaned datasets
- **Complete audit trail** of all cleaning operations

### **YAML-Based Configuration**

- **Fully decoupled** configuration for reproducibility
- **Pipeline versioning** and easy sharing
- **Template generation** with `datacmp init`

### **Command-Line Interface**

- **Run pipelines** directly from terminal
- **Generate config files** with defaults
- **Progress tracking** and verbose logging

---

### **Comparison: v2.0 → v3.0**

| Feature             | v2.0            | v3.0             |
| ------------------- | --------------- | ---------------- |
| **API Style**       | Functional only | OOP + Functional |
| **Method Chaining** | ❌              | ✅               |
| **Type Hints**      | Partial         | Complete         |
| **Logging**         | print()         | logging module   |
| **Visualizations**  | ❌              | ✅ (3 types)     |
| **HTML Reports**    | ❌              | ✅ (styled)      |
| **Correlations**    | ❌              | ✅               |
| **CLI Subcommands** | ❌              | ✅               |
| **Test Coverage**   | None            | Comprehensive    |
| **Packaging**       | setup.py        | pyproject.toml   |

---

## Installation

### From PyPI (Recommended)

```bash
pip install datacmp
```

### From Source

```bash
git clone https://github.com/MoustafaMohamed01/datacmp.git
cd datacmp
pip install -e .
```

### With Optional Dependencies

```bash
# For full features
pip install datacmp[full]

# For development
pip install datacmp[dev]
```

---

## Quick Start

### Python API

```python
from datacmp import DataCmp

# Load and process your data
cmp = DataCmp("data.csv")

# Clean, profile, and export in one chain
cmp.clean().profile().export("report.html")

# Or use individual methods
cmp = DataCmp("data.csv")
cmp.clean(outliers=True, duplicates=True)
cmp.profile(detailed=True)
cmp.visualize(output_dir="./plots")
cmp.export("cleaned_data.csv")
```

### Command-Line Interface

```bash
# Run complete pipeline
datacmp run data.csv --config config.yaml --export cleaned.csv --report report.html

# Create default config file
datacmp init my_config.yaml

# Show version
datacmp version
```

---

## Usage Examples

### Example 1: Basic Cleaning

```python
from datacmp import DataCmp

# Initialize with auto-clean
cmp = DataCmp("messy_data.csv", auto_clean=True)

# Export cleaned data
cmp.export("clean_data.csv")

# View cleaning log
print(cmp.get_cleaning_log())
```

### Example 2: Custom Configuration

```python
from datacmp import DataCmp

# Define custom config
config = {
    "cleaning": {
        "threshold_drop": 0.3,  # Drop columns with >30% missing
        "fill_strategy": {
            "numeric": "mean",
            "categorical": "mode"
        },
        "outlier_handling": {
            "enabled": True,
            "action": "remove"  # Remove outliers instead of capping
        }
    }
}

# Use custom config
cmp = DataCmp("data.csv", config=config)
cmp.clean().profile()
```

### Example 3: Method Chaining

```python
from datacmp import DataCmp

result = (
    DataCmp("data.csv")
    .clean(columns=True, missing=True, outliers=True)
    .profile(detailed=True)
    .visualize(output_dir="./plots")
    .export("report.html")
)
```

### Example 4: Programmatic Pipeline

```python
from datacmp import run_pipeline

# Run entire pipeline with one function
df_cleaned = run_pipeline(
    data="data.csv",
    config_path="config.yaml",
    export_csv_path="cleaned.csv",
    export_report_path="report.html"
)
```

---

## Configuration

### Example `config.yaml`

```yaml
library_name: datacmp
version: 3.0.0
author: Moustafa Mohamed

cleaning:
  threshold_drop: 0.45
  fill_strategy:
    numeric: median
    categorical: mode
  outlier_handling:
    enabled: true
    method: iqr
    iqr_multiplier: 1.5
    action: cap

drop_duplicates: true

profiling:
  include_more_stats: true
  compute_correlations: true
```

### Configuration Options

| Option                      | Description                                             | Default  |
| --------------------------- | ------------------------------------------------------- | -------- |
| `threshold_drop`            | Drop columns with missing ratio above this              | `0.45`   |
| `fill_strategy.numeric`     | Strategy for numeric columns (`mean`, `median`, `mode`) | `median` |
| `fill_strategy.categorical` | Strategy for categorical columns (`mode`)               | `mode`   |
| `outlier_handling.enabled`  | Enable outlier detection                                | `true`   |
| `outlier_handling.method`   | Detection method (`iqr`)                                | `iqr`    |
| `outlier_handling.action`   | Action to take (`cap`, `remove`)                        | `cap`    |
| `drop_duplicates`           | Remove duplicate rows                                   | `true`   |

---

## Visualizations

Datacmp automatically generates:

- **Missing Value Heatmaps** - Visualize patterns in missing data
- **Correlation Heatmaps** - Identify relationships between features
- **Distribution Plots** - Understand feature distributions

```python
cmp = DataCmp("data.csv")
cmp.clean().profile()
cmp.visualize(output_dir="./plots")
```

---

## Reports

### HTML Reports

Beautiful, interactive HTML reports with:

- Dataset overview and statistics
- Cleaning operation log
- Embedded visualizations
- Responsive design

```python
cmp.export("report.html")
```

### Text Reports

Lightweight text reports for quick inspection:

```python
cmp.export("report.txt")
```

---

## API Reference

### DataCmp Class

```python
DataCmp(data, config=None, auto_clean=False)
```

**Methods:**

- `clean(columns=True, missing=True, outliers=True, duplicates=True)` - Clean the dataset
- `profile(detailed=True)` - Generate profiling information
- `visualize(output_dir=None)` - Create visualizations
- `export(output, format=None, include_plots=True)` - Export results
- `reset()` - Reset to original DataFrame
- `get_summary()` - Get dataset summary string
- `get_cleaning_log()` - Get list of cleaning operations

---

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
git clone https://github.com/MoustafaMohamed01/datacmp.git
cd datacmp
pip install -e ".[dev]"
```

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author

**Moustafa Mohamed**

- Email: moustafa.mh.mohamed@gmail.com
- Linkedin: [Moustafa Mohamed](https://www.linkedin.com/in/moustafamohamed01/)
- GitHub: [MoustafaMohamed01](https://github.com/MoustafaMohamed01)
- Kaggle: [moustafamohamed01](https://www.kaggle.com/moustafamohamed01)

---

## Show Your Support

Give a ⭐️ if this project helped you!

---

## Resources

- [Documentation](https://github.com/MoustafaMohamed01/datacmp#readme)
- [Issue Tracker](https://github.com/MoustafaMohamed01/datacmp/issues)
- [PyPI Package](https://pypi.org/project/datacmp/)
