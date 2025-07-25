# datacmp – Exploratory Data Analysis & Data Cleaning Toolkit

[![PyPI version](https://img.shields.io/pypi/v/datacmp.svg)](https://pypi.org/project/datacmp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

datacmp is a lightweight, modular Python library designed to simplify and accelerate exploratory data analysis (EDA) and data cleaning tasks in data science workflows. It provides structured insights, intelligent preprocessing, and configuration flexibility through a YAML-based pipeline.

Available on PyPI: [https://pypi.org/project/datacmp/](https://pypi.org/project/datacmp/)

---

## Key Features

Data Overview & Profiling

* Generates concise, tabulated summaries of your dataset
* Reports missing values, data types, and unique counts
* Optional extended statistics: mean, median, std, skewness, kurtosis
* Column type breakdown: numeric, categorical, datetime

Column Name Standardization

* Automatically cleans and renames columns (lowercase, no spaces)
* Logs name transformations for traceability

Missing Value & Outlier Handling

* Drops columns exceeding a missing value threshold
* Fills missing values using configurable strategies (mean, median, mode)
* Detects and handles outliers using IQR (remove or cap)
* Optionally removes duplicate rows

YAML-Based Configuration

* Easy customization of fill strategies, thresholds, and outlier handling
* Fully decoupled from code logic for reproducibility

Export Capabilities (v2.0+)

* Save cleaned datasets as CSV
* Generate human-readable reports in TXT format

Command-Line Interface (v2.0+)

* Run the full pipeline directly from terminal using a CLI wrapper

---

## Installation

Install from PyPI:

```bash
pip install datacmp
```

Or install from source:

```bash
git clone https://github.com/MoustafaMohamed01/datacmp.git
cd datacmp
pip install -r requirements.txt
```

Requirements:

* pandas
* tabulate
* PyYAML

---

## Configuration (config.yaml)

Example configuration file:

```yaml
cleaning:
  fill_strategy:
    categorical: mode
    numeric: median
  outlier_handling:
    enabled: true
    method: iqr
    action: cap
    iqr_multiplier: 1.5
  threshold_drop: 0.45
drop_duplicates: true
profiling:
  include_more_stats: true
```

---

## Usage (Python)

Basic usage with config:

```python
import pandas as pd
from datacmp.run_pipeline import run_pipeline

df = pd.read_csv("data.csv")
cleaned_df = run_pipeline(
    df,
    config_path="config.yaml",
    export_csv_path="cleaned.csv",
    export_report_path="summary.txt"
)
```

---

## Usage (CLI)

Run from the command line:

```bash
python cli.py --file data.csv --config config.yaml --export_csv cleaned.csv --export_report summary.txt
```

Available arguments:

* --file: input CSV file (required)
* --config: YAML config file (default = config.yaml)
* --export_csv: optional output path for cleaned CSV
* --export_report: optional output path for summary TXT

---

## Project Structure

```
datacmp/
├── datacmp/
│   ├── __init__.py
│   ├── column_cleaning.py       # Column renaming logic
│   ├── data_cleaning.py         # Missing value & outlier processing
│   ├── detailed_info.py         # Dataset summaries & profiling
│   ├── run_pipeline.py          # Main pipeline logic
├── cli.py                       # CLI entry point
├── config.yaml                  # Example configuration
├── setup.py                     # Packaging & dependencies
├── README.md
├── LICENSE
```

---

## Release History

🔹 v1.0.0 – Initial release

* Data profiling, missing value handling, column name cleaning, YAML config support

🔹 v2.0.0 – Major update

* Added CLI support
* Added CSV & TXT export options
* Enhanced profiling (column type summary)

View changelog & releases → [https://github.com/MoustafaMohamed01/datacmp/releases](https://github.com/MoustafaMohamed01/datacmp/releases)

---

## License

Released under the MIT License. See [LICENSE](LICENSE) for details.

---

## Author

Developed by [Moustafa Mohamed](https://github.com/MoustafaMohamed01)

[LinkedIn](https://www.linkedin.com/in/moustafamohamed01/) • [Kaggle](https://www.kaggle.com/moustafamohamed01)

---
