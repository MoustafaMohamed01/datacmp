# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned Features

- Integration with Polars for faster processing
- AI-powered data quality suggestions (optional OpenAI integration)
- Advanced anomaly detection algorithms
- Interactive dashboards for reports
- Support for more file formats (Parquet, JSON, Excel)

---

## [3.0.0] - 2025-10-30

### Major Release - Complete Library Refactor

This is a major release with breaking changes and significant enhancements. Datacmp has been completely refactored with a modern architecture, improved API, and extensive new features.

### Added

#### Core Features

- **New `DataCmp` class** - Object-oriented API with method chaining support
- **Method chaining** - Fluent interface: `DataCmp("data.csv").clean().profile().export("report.html")`
- **Auto-clean functionality** - Optional automatic cleaning on initialization
- **State management** - `reset()` method to revert to original DataFrame
- **Caching system** - Profile data caching for better performance

#### Advanced Profiling

- **Correlation analysis** - Pearson, Spearman, and Kendall methods
- **Extended statistics** - Skewness, kurtosis, quantiles
- **Memory usage reporting** - Track DataFrame memory consumption
- **Column type detection** - Automatic classification of numeric, categorical, datetime columns
- **Statistical profiling** - Comprehensive stats for numeric and categorical columns

#### Visualizations

- **Missing value heatmaps** - Visualize patterns in missing data
- **Correlation heatmaps** - Beautiful correlation matrices
- **Distribution plots** - Histograms for numeric features
- **High-resolution exports** - 300 DPI PNG output
- **Customizable output** - Save to directory or display inline

#### Reporting

- **HTML reports** - Beautiful, modern styled reports with embedded visualizations
- **Text reports** - Lightweight TXT reports for quick inspection
- **Comprehensive audit trails** - Complete log of all cleaning operations
- **Export flexibility** - Support for CSV, HTML, and TXT formats

#### CLI Enhancements

- **Subcommands** - `run`, `init`, `version` commands
- **Config generation** - `datacmp init` creates default config
- **Better help messages** - Improved documentation in CLI
- **Verbose/quiet modes** - Control output verbosity

#### Developer Experience

- **Type hints** - Complete type annotations throughout codebase
- **Comprehensive logging** - Structured logging with `logging` module
- **Test suite** - pytest-based tests with >80% coverage
- **Modern packaging** - `pyproject.toml` for Python 3.10+
- **Modular architecture** - Clear separation of concerns

### Changed

#### Breaking Changes

- **API redesign** - New `DataCmp` class replaces functional API (old API still available via `run_pipeline`)
- **Import structure** - New module organization (see migration guide below)
- **Configuration format** - Enhanced YAML structure with new options
- **Python requirement** - Now requires Python 3.10+ (was 3.7+)

#### Improvements

- **Performance** - Optimized correlation and statistical computations
- **Error handling** - Better error messages and handling
- **Code quality** - PEP8 compliant, Black formatted
- **Documentation** - Complete rewrite with examples and API reference

### Fixed

- **Column name cleaning** - Better handling of special characters
- **Missing value strategies** - Fixed edge cases in mode calculation
- **Outlier detection** - Improved IQR calculation for edge cases
- **Memory leaks** - Fixed DataFrame copying issues

### Documentation

- **README.md** - Complete rewrite with badges, examples, and API reference
- **CONTRIBUTING.md** - Comprehensive contribution guidelines
- **Docstrings** - Google-style docstrings throughout

### Project Structure

```
datacmp/
├── datacmp/
│   ├── core/          # Main DataCmp class
│   ├── cleaning/      # Cleaning modules
│   ├── profiling/     # Profiling modules
│   ├── pipeline/      # Pipeline execution
│   ├── visuals/       # Visualization and reporting
│   ├── cli/           # Command-line interface
│   └── utils/         # Utilities and helpers
└── docs/              # Documentation
```

### Dependencies

- Added: `matplotlib>=3.6.0`, `seaborn>=0.12.0`
- Updated: `pandas>=1.5.0`, `numpy>=1.23.0`
- Minimum Python version: 3.10

### Migration Guide (v2.0 → v3.0)

**Old API (still works):**

```python
from datacmp import run_pipeline
df = run_pipeline("data.csv", config_path="config.yaml")
```

**New API (recommended):**

```python
from datacmp import DataCmp
cmp = DataCmp("data.csv", config="config.yaml")
cmp.clean().profile().export("report.html")
```

**Import Changes:**

```python
# Old
from datacmp.detailed_info import get_detailed
from datacmp.column_cleaning import clean_column_names

# New
from datacmp.profiling.summary import generate_summary
from datacmp.cleaning.columns import clean_column_names
```

---

## Upgrade Instructions

### From v2.0 to v3.0

1. **Update Python version:**

   ```bash
   # Ensure Python 3.10+
   python --version
   ```

2. **Install new version:**

   ```bash
   pip install --upgrade datacmp
   ```

3. **Update imports** (if using internal modules):

   ```python
   # Old imports still work, but new structure is recommended
   from datacmp import DataCmp  # New recommended API
   ```

4. **Update configuration** (optional new fields):

   ```yaml
   profiling:
     include_more_stats: true
     compute_correlations: true # New option
   ```

5. **Test your code:**

   ```python
   # Old API still supported
   from datacmp import run_pipeline
   df = run_pipeline("data.csv")  # ✅ Still works

   # New API recommended
   from datacmp import DataCmp
   cmp = DataCmp("data.csv").clean().profile()  # ✅ New way
   ```

---

## Deprecation Notices

### v3.0.0

- **None** - All v2.0 functionality remains available

### Future Deprecations

- **v4.0.0** (planned): May deprecate old functional API in favor of OOP API
- **v4.0.0** (planned): May drop Python 3.10 support in favor of 3.11+

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

---

## Links

- **Repository:** https://github.com/MoustafaMohamed01/datacmp
- **PyPI:** https://pypi.org/project/datacmp/
- **Issues:** https://github.com/MoustafaMohamed01/datacmp/issues
- **Changelog:** https://github.com/MoustafaMohamed01/datacmp/blob/main/CHANGELOG.md

---

**Legend:**

- Major release
- New features
- Changes
- Bug fixes
- Documentation
- Project structure
- Dependencies
- Migration guide
