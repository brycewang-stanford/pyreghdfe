# ⚠️ ARCHIVED - This repository is no longer maintained

**All functionality has been moved to [Py-Stata-Commands](https://github.com/brycewang-stanford/Py-Stata-Commands)**

---

# PyRegHDFE

[![Python Version](https://img.shields.io/pypi/pyversions/pyreghdfe)](https://pypi.org/project/pyreghdfe/)
[![PyPI Version](https://img.shields.io/pypi/v/pyreghdfe)](https://pypi.org/project/pyreghdfe/)
[![License](https://img.shields.io/github/license/brycewang-stanford/pyreghdfe)](LICENSE)

**⚠️ MIGRATION NOTICE**: This package has been integrated into the unified **Py-Stata-Commands** package.

## 🔄 Migration Instructions

**Old:**
```bash
pip install pyreghdfe
```
```python
from pyreghdfe import reghdfe
result = reghdfe(data=df, y='wage', x=['experience'], fe=['firm_id'])
```

**New:**
```bash
pip install py-stata-commands
```
```python
from py_stata_commands import reghdfe
result = reghdfe.reghdfe(data=df, y='wage', x=['experience'], fe=['firm_id'])
```

## 🎯 Why the Change?

The new unified package provides:
- **Single installation** for all Stata-equivalent commands (tabulate, egen, reghdfe, winsor2)
- **Consistent API** across all modules
- **Better documentation** and examples
- **Easier maintenance** and updates

## 📖 New Documentation

Visit the new repository for complete documentation:
**https://github.com/brycewang-stanford/Py-Stata-Commands**

---

*This repository is archived and will not receive further updates. Please migrate to the new package.*