
# Datacmp  
[![PyPI version](https://img.shields.io/pypi/v/datacmp.svg)](https://pypi.org/project/datacmp/) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

**Datacmp** is a lightweight and modular Python library for **exploratory data analysis (EDA)** and **data cleaning** using `pandas`.  
It helps you quickly generate clean summaries, standardize column names, and handle missing values — all with professional tabulated outputs and optional YAML configuration.

🔗 **Available on PyPI**: [https://pypi.org/project/datacmp/](https://pypi.org/project/datacmp/)

---

## Features

- **Dataset Summary**
  - Report total rows, columns, data types, missing values, and basic statistics
- **Column Name Cleaning**
  - Standardize column names for readability and consistency
- **Missing Value Handling** (`clean_missing_data`)
  - Convert data types (numeric and datetime)
  - Drop columns with excessive missing values
  - Fill missing values using intelligent strategies (mean, median, mode)
  - Optionally remove duplicate rows
- **YAML Configuration Support**
  - Customize behavior using `config.yaml` without touching your code
- **Formatted Output**
  - Display insights with beautiful, readable tables powered by `tabulate`

---

## Installation

Install directly from PyPI:

```bash
pip install datacmp
```

Or clone the repository:

```bash
git clone https://github.com/MoustafaMohamed01/datacmp.git
cd dataforge
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install pandas tabulate
```

---

## Project Structure

```
datacmp/
│
├── datacmp/
│   ├── __init__.py            # Main package initializer
│   ├── column_cleaning.py     # Functions to clean column names
│   ├── detailed_info.py       # EDA functions for summarizing datasets
│   ├── data_cleaning.py       # Functions to handle missing values intelligently
│
├── config.yaml                # Optional configuration file
├── LICENSE                    # MIT license
├── requirements.txt           # Project dependencies
├── setup.py                   # Setup script for packaging
├── README.md                  # Project documentation
```

---

## Requirements

- `pandas`
- `tabulate`

All required packages are listed in [`requirements.txt`](requirements.txt).

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

Developed by [Moustafa Mohamed](https://github.com/MoustafaMohamed01)

- [LinkedIn](https://www.linkedin.com/in/moustafamohamed01/)
- [Kaggle](https://www.kaggle.com/moustafamohamed01)
```
