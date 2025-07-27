# ⚠️ This Repository Has Been Archived

This repository has been **archived** and is no longer maintained. 

All functionality from `pyreghdfe` has been integrated into the unified **Py-Stata-Commands** package.

## 🔗 New Repository

Please use the new unified repository:
**https://github.com/brycewang-stanford/Py-Stata-Commands**

## 🚀 New Installation

```bash
pip install py-stata-commands
```

## 📖 New Usage

```python
from py_stata_commands import reghdfe

# Same functionality, new location
result = reghdfe.reghdfe(
    data=df,
    depvar='wage',
    regressors=['experience', 'education'],
    absorb=['firm_id', 'year'],
    cluster='firm_id'
)
```

## 📚 Benefits of the New Package

- **Unified installation**: All Stata-equivalent commands in one package
- **Consistent API**: Familiar syntax across all modules
- **Better maintenance**: Single repository for all related functionality
- **Comprehensive documentation**: Complete examples and guides

---

**Migration**: Replace `import pyreghdfe` with `from py_stata_commands import reghdfe`