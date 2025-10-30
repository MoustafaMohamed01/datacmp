# Contributing to Datacmp

First off, thank you for considering contributing to Datacmp!

It's people like you that make Datacmp such a great tool for the data science community.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Style Guidelines](#style-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)
- [Testing](#testing)
- [Documentation](#documentation)

---

## Code of Conduct

This project and everyone participating in it is governed by our commitment to provide a welcoming and inspiring community for all. Please be respectful and constructive in your interactions.

### Our Standards

**Examples of behavior that contributes to a positive environment:**

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Examples of unacceptable behavior:**

- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information without explicit permission
- Other conduct which could reasonably be considered inappropriate

---

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the [issue tracker](https://github.com/MoustafaMohamed01/datacmp/issues) to avoid duplicates.

**When submitting a bug report, please include:**

- **Clear and descriptive title**
- **Detailed description** of the issue
- **Steps to reproduce** the behavior
- **Expected behavior**
- **Actual behavior**
- **Screenshots** (if applicable)
- **Environment details:**
  - OS: [e.g., Windows 10, macOS 13.0, Ubuntu 22.04]
  - Python version: [e.g., 3.10.5]
  - Datacmp version: [e.g., 3.0.0]
  - Relevant dependencies versions

**Example Bug Report:**

```markdown
**Bug Description:**
Missing value handling fails when DataFrame contains mixed types

**Steps to Reproduce:**

1. Create DataFrame with mixed numeric/string columns
2. Call `cmp.clean(missing=True)`
3. Error occurs

**Expected Behavior:**
Should handle mixed types gracefully

**Actual Behavior:**
TypeError: Cannot compute mean of string column

**Environment:**

- OS: Ubuntu 22.04
- Python: 3.10.8
- Datacmp: 3.0.0
```

### Suggesting Enhancements

Enhancement suggestions are tracked as [GitHub issues](https://github.com/MoustafaMohamed01/datacmp/issues).

**When suggesting an enhancement, please include:**

- **Clear and descriptive title**
- **Detailed description** of the proposed functionality
- **Use case** explaining why this would be useful
- **Possible implementation** approach (if you have ideas)
- **Examples** of how it would be used

### Pull Requests

We actively welcome your pull requests!

**Areas where contributions are especially welcome:**

- Bug fixes
- New cleaning strategies
- Additional visualization types
- Performance improvements
- Documentation improvements
- Test coverage expansion
- New examples and tutorials

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Git
- pip

### Setting Up Development Environment

1. **Fork the repository** on GitHub

2. **Clone your fork:**

```bash
git clone https://github.com/YOUR_USERNAME/datacmp.git
cd datacmp
```

3. **Create a virtual environment:**

```bash
# Using venv
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

4. **Install development dependencies:**

```bash
pip install -e ".[dev]"
```

5. **Create a new branch:**

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

---

## Development Workflow

### 1. Make Your Changes

- Write clear, readable code
- Follow the style guidelines (see below)
- Add tests for new functionality
- Update documentation as needed

### 2. Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=datacmp --cov-report=html

# Run specific test file
pytest tests/test_cleaning.py

# Run specific test
pytest tests/test_cleaning.py::TestColumnCleaning::test_clean_column_names
```

### 3. Check Code Style

```bash
# Format code with Black
black datacmp/

# Check with flake8
flake8 datacmp/

# Type checking with mypy (optional)
mypy datacmp/
```

### 4. Update Documentation

If you've changed functionality:

- Update docstrings
- Update README.md if needed
- Add examples to `examples/` directory
- Update CHANGELOG.md

### 5. Commit Your Changes

```bash
git add .
git commit -m "feat: add new correlation method"
```

See [Commit Messages](#commit-messages) section for guidelines.

### 6. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 7. Create Pull Request

Go to the [original repository](https://github.com/MoustafaMohamed01/datacmp) and create a pull request from your branch.

---

## Style Guidelines

### Python Style Guide

We follow [PEP 8](https://pep8.org/) with some modifications:

- **Line length:** 100 characters (configured in Black)
- **Indentation:** 4 spaces
- **Quotes:** Double quotes for strings (Black default)

### Code Formatting

We use **Black** as our code formatter:

```bash
black datacmp/
```

Configuration is in `pyproject.toml`:

```toml
[tool.black]
line-length = 100
target-version = ['py310']
```

### Linting

We use **Flake8** for linting:

```bash
flake8 datacmp/
```

### Type Hints

- Use type hints for all function signatures
- Use `typing` module for complex types

**Example:**

```python
from typing import Optional, List, Dict, Any
import pandas as pd

def clean_data(
    df: pd.DataFrame,
    config: Optional[Dict[str, Any]] = None
) -> tuple[pd.DataFrame, List[str]]:
    """Clean the input DataFrame."""
    pass
```

### Docstrings

Use **Google-style docstrings**:

```python
def example_function(param1: str, param2: int) -> bool:
    """
    Brief description of function.

    Longer description if needed, explaining what the function does,
    any important details, or edge cases.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ValueError: When invalid input is provided

    Example:
        >>> result = example_function("test", 42)
        >>> print(result)
        True
    """
    pass
```

### Naming Conventions

- **Functions/methods:** `lowercase_with_underscores`
- **Classes:** `PascalCase`
- **Constants:** `UPPERCASE_WITH_UNDERSCORES`
- **Private methods:** `_leading_underscore`
- **Module names:** `lowercase_with_underscores`

---

## Commit Messages

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

### Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types

- **feat:** A new feature
- **fix:** A bug fix
- **docs:** Documentation only changes
- **style:** Code style changes (formatting, missing semicolons, etc.)
- **refactor:** Code changes that neither fix a bug nor add a feature
- **perf:** Performance improvements
- **test:** Adding missing tests or correcting existing tests
- **chore:** Changes to build process or auxiliary tools
- **ci:** Changes to CI configuration files and scripts

### Examples

```bash
feat: add Spearman correlation support

fix: handle missing values in correlation computation

docs: update README with new visualization examples

test: add tests for outlier detection

refactor: simplify missing value handling logic

perf: optimize correlation matrix computation for large datasets
```

### Breaking Changes

For breaking changes, add `BREAKING CHANGE:` in the footer:

```bash
feat: change API for DataCmp initialization

BREAKING CHANGE: `auto_clean` parameter now defaults to False instead of True
```

---

## Pull Request Process

### Before Submitting

✅ **Checklist:**

- [ ] Code follows style guidelines
- [ ] All tests pass locally
- [ ] New tests added for new functionality
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] No merge conflicts with main branch
- [ ] Commit messages follow conventions

### PR Template

When creating a pull request, please use this template:

```markdown
## Description

Brief description of changes

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing

Describe the tests you ran

## Checklist

- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have commented my code where necessary
- [ ] I have updated the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix/feature works
- [ ] New and existing tests pass locally

## Related Issues

Closes #123
```

### Review Process

1. **Automated checks** will run (tests, linting)
2. **Code review** by maintainers
3. **Feedback addressed** if requested
4. **Approval** and merge by maintainers

### After Your PR is Merged

- Delete your branch (if it was in the main repo)
- Pull the latest changes: `git pull upstream main`
- Celebrate! You're now a datacmp contributor!

---

## Testing

### Running Tests

```bash
# All tests
pytest

# Specific module
pytest tests/test_cleaning.py

# With coverage report
pytest --cov=datacmp --cov-report=html

# Verbose output
pytest -v

# Stop on first failure
pytest -x
```

### Writing Tests

- Place tests in `tests/` directory
- Name test files `test_*.py`
- Name test functions `test_*`
- Use descriptive test names
- Test edge cases and error conditions

**Example Test:**

```python
import pytest
import pandas as pd
from datacmp.cleaning.columns import clean_column_names

class TestColumnCleaning:
    def test_clean_column_names_basic(self):
        """Test basic column name cleaning."""
        df = pd.DataFrame({"First Name": [1, 2], "Last Name ": [3, 4]})
        cleaned_df, log = clean_column_names(df)

        assert list(cleaned_df.columns) == ["first_name", "last_name"]
        assert len(log) == 2

    def test_clean_column_names_special_chars(self):
        """Test cleaning of special characters."""
        df = pd.DataFrame({"Age@#$": [1, 2]})
        cleaned_df, log = clean_column_names(df)

        assert list(cleaned_df.columns) == ["age"]
```

### Test Coverage

We aim for **>80% test coverage**. Check coverage with:

```bash
pytest --cov=datacmp --cov-report=term-missing
```

---

## Documentation

### Types of Documentation

1. **Code Documentation** (docstrings)
2. **README.md** (user-facing documentation)
3. **Examples** (`examples/` directory)
4. **API Reference** (generated from docstrings)

### Writing Good Documentation

**Do:**

- ✅ Use clear, simple language
- ✅ Provide examples
- ✅ Explain the "why" not just the "what"
- ✅ Keep it up-to-date with code changes

**Don't:**

- ❌ Assume prior knowledge
- ❌ Use jargon without explanation
- ❌ Write documentation that duplicates code
- ❌ Forget to update docs when code changes

### Example Documentation

```python
def compute_correlations(df: pd.DataFrame, method: str = "pearson") -> pd.DataFrame:
    """
    Compute correlation matrix for numeric columns.

    This function calculates pairwise correlations between all numeric
    columns in the DataFrame using the specified method. It automatically
    filters out non-numeric columns.

    Args:
        df: Input DataFrame
        method: Correlation method to use. Options:
            - 'pearson': Standard correlation coefficient (default)
            - 'spearman': Spearman rank correlation
            - 'kendall': Kendall Tau correlation

    Returns:
        Correlation matrix as DataFrame with numeric columns only.
        Returns None if fewer than 2 numeric columns.

    Raises:
        ValueError: If method is not one of the supported options

    Example:
        >>> df = pd.DataFrame({
        ...     'A': [1, 2, 3, 4, 5],
        ...     'B': [2, 4, 6, 8, 10]
        ... })
        >>> corr = compute_correlations(df, method='pearson')
        >>> print(corr.loc['A', 'B'])
        1.0

    Note:
        This function requires at least 2 numeric columns in the
        DataFrame. Non-numeric columns are automatically ignored.
    """
    pass
```

---

## Questions?

If you have questions, feel free to:

- Open an issue with the `question` label
- Email: moustafa.mh.mohamed@gmail.com
- Check existing [discussions](https://github.com/MoustafaMohamed01/datacmp/discussions)

---

## Recognition

Contributors will be recognized in:

- **README.md** - Contributors section
- **Release notes** - For significant contributions
- **GitHub contributors** page

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to Datacmp!**
