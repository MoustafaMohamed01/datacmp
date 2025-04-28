# DataForge  
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

**DataForge** is a lightweight Python library designed to simplify exploratory data analysis and data cleaning for pandas DataFrames.  
It helps you quickly generate detailed dataset summaries and clean messy column names, all with clean and customizable outputs.

---

## Features

- **Dataset Summary**  
  - Display number of rows and columns
  - List data types, null counts, and non-null counts
  - Calculate mean values for numeric columns
- **Data Cleaning**  
  - Clean column names for better consistency and readability
- **Configuration Support**  
  - Use `config.yaml` to customize behavior without modifying the code
- **Tabulated Output**  
  - Generate clear and professional summaries with the `tabulate` library

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/MoustafaMohamed01/dataforge.git
cd dataforge
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pandas tabulate
```

---

##  Project Structure

```
dataforge/
│
├── dataforge/
│   ├── __init__.py          # Main package initializer
│   ├── column_cleaner.py    # Functions for cleaning column names
│   ├── detailed_info.py     # Functions for generating dataset summaries
│
├── config.yaml              # Configuration file
├── LICENSE                  # Project license (MIT)
├── requirements.txt         # Project dependencies
├── setup.py                 # Installation and packaging
├── README.md                
```

---

##  Requirements

- `pandas`
- `tabulate`

All dependencies are listed in [`requirements.txt`](requirements.txt).

---

##  License

This project is licensed under the [MIT License](LICENSE).

---

##  Author

Developed by [Moustafa Mohamed](https://github.com/MoustafaMohamed01)  

- [LinkedIn](https://www.linkedin.com/in/moustafamohamed01/)
- [Kaggle](https://www.kaggle.com/moustafamohamed01)
