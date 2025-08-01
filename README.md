# RegHDFE

**Note: This package continues to be maintained. Additionally, `reghdfe` functionality is also integrated into [StatsPAI](https://github.com/brycewang-stanford/StatsPAI/) for users who prefer the unified ecosystem.**

---

[![Python Version](https://img.shields.io/pypi/pyversions/reghdfe)](https://pypi.org/project/reghdfe/)
[![PyPI Version](https://img.shields.io/pypi/v/reghdfe)](https://pypi.org/project/reghdfe/)
[![License](https://img.shields.io/github/license/brycewang-stanford/pyreghdfe)](LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/reghdfe)](https://pypi.org/project/reghdfe/)

Python implementation of Stata's reghdfe for high-dimensional fixed effects regression.

## � Installation

```bash
pip install reghdfe
```

## 📖 Basic Usage

```python
from reghdfe import reghdfe
result = reghdfe(data=df, y='wage', x=['experience'], fe=['firm_id'])
```

## 🔗 Integration Options

This package is **actively maintained** as a standalone library. For users who prefer a unified ecosystem with additional econometric and statistical tools, `reghdfe` functionality is also available through:

- **[StatsPAI](https://github.com/brycewang-stanford/StatsPAI/)** - Stats + Econometrics + ML + AI + LLMs

## 🔗 Related Projects

- **[StatsPAI](https://github.com/brycewang-stanford/StatsPAI/)** - StatsPAI = Stats + Econometrics + ML + AI + LLMs  
- **[PyStataR](https://github.com/brycewang-stanford/PyStataR)** - Unified Stata-equivalent commands and R functions

## 📚 Documentation

For detailed documentation, examples, and API reference, please visit our [GitHub repository](https://github.com/brycewang-stanford/reghdfe).

---

**This package is actively maintained.** For questions, bug reports, or feature requests, please open an issue on GitHub.