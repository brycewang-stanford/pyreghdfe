# PyRegHDFE

## 🚀 Installation

```bash
pip install pyreghdfe
```e: This package continues to be maintained. Additionally, `reghdfe` functionality is also integrated into [StatsPAI](https://github.com/brycewang-stanford/StatsPAI/## 📚 Documentation

For detailed API reference and additional examples, visit our [GitHub repository](https://github.com/brycewang-stanford/pyreghdfe).

## 🤝 Contributing

We welcome contributions! Please feel free to:
- Report bugs or request features via [GitHub Issues](https://github.com/brycewang-stanford/pyreghdfe/issues)
- Submit pull requests for improvements
- Share your use cases and exampless who prefer the unified ecosystem.**

---

[![Python Version](https://img.shields.io/pypi/pyversions/pyreghdfe)](https://pypi.org/project/pyreghdfe/)
[![PyPI Version](https://img.shields.io/pypi/v/pyreghdfe)](https://pypi.org/project/pyreghdfe/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://img.shields.io/pypi/dm/pyreghdfe)](https://pypi.org/project/pyreghdfe/)

Python implementation of Stata's reghdfe for high-dimensional fixed effects regression.

##  Installation

```bash
pip install reghdfe
```

## 📖 Quick Start

### Basic Example

```python
import pandas as pd
import numpy as np
from reghdfe import reghdfe

# Create sample data
np.random.seed(42)
n = 1000
data = pd.DataFrame({
    'wage': np.random.normal(10, 2, n),
    'experience': np.random.normal(5, 2, n),
    'education': np.random.normal(12, 3, n),
    'firm_id': np.random.choice(range(100), n),
    'year': np.random.choice(range(2010, 2020), n)
})

# Run regression with firm fixed effects
result = reghdfe(
    data=data,
    y='wage',
    x=['experience', 'education'],
    fe=['firm_id']
)

# Display results
print(result.summary())
```

### Advanced Usage Examples

#### 1. Multiple Fixed Effects

```python
# Regression with firm and year fixed effects
result = reghdfe(
    data=data,
    y='wage',
    x=['experience', 'education'],
    fe=['firm_id', 'year']  # Multiple dimensions
)
print(result.summary())
```

#### 2. Cluster-Robust Standard Errors

```python
# One-way clustering
result = reghdfe(
    data=data,
    y='wage',
    x=['experience', 'education'],
    fe=['firm_id'],
    cluster=['firm_id']  # Cluster by firm
)

# Two-way clustering
result = reghdfe(
    data=data,
    y='wage',
    x=['experience', 'education'],
    fe=['firm_id'],
    cluster=['firm_id', 'year']  # Cluster by firm and year
)
```

#### 3. Weighted Regression

```python
# Add weights to your data
data['weight'] = np.random.uniform(0.5, 2.0, len(data))

# Run weighted regression
result = reghdfe(
    data=data,
    y='wage',
    x=['experience', 'education'],
    fe=['firm_id'],
    weights='weight'
)
```

#### 4. No Fixed Effects (OLS)

```python
# Simple OLS regression
result = reghdfe(
    data=data,
    y='wage',
    x=['experience', 'education'],
    fe=None  # No fixed effects
)
```

## Working with Results

### Accessing Coefficients and Statistics

```python
result = reghdfe(data=data, y='wage', x=['experience', 'education'], fe=['firm_id'])

# Get coefficients
coefficients = result.coef
print("Coefficients:", coefficients)

# Get standard errors
std_errors = result.se
print("Standard Errors:", std_errors)

# Get t-statistics
t_stats = result.tstat
print("T-statistics:", t_stats)

# Get p-values
p_values = result.pvalue
print("P-values:", p_values)

# Get confidence intervals
conf_int = result.conf_int()
print("95% Confidence Intervals:", conf_int)

# Get R-squared
print(f"R-squared: {result.rsquared:.4f}")
print(f"Adjusted R-squared: {result.rsquared_adj:.4f}")
```

### Summary Statistics

```python
# Full regression summary
print(result.summary())

# Detailed summary with additional statistics
print(result.summary(show_dof=True))
```

## 🔧 Advanced Configuration

### Custom Absorption Options

```python
result = reghdfe(
    data=data,
    y='wage',
    x=['experience', 'education'],
    fe=['firm_id'],
    absorb_tolerance=1e-10,  # Higher precision
    drop_singletons=True,    # Drop singleton groups
    absorb_method='lsmr'     # Alternative solver
)
```

### Different Covariance Types

```python
# Robust standard errors (default)
result = reghdfe(data=data, y='wage', x=['experience'], fe=['firm_id'], 
                cov_type='robust')

# Clustered standard errors
result = reghdfe(data=data, y='wage', x=['experience'], fe=['firm_id'], 
                cov_type='cluster', cluster=['firm_id'])
```

## Comparison with Stata

This package aims to replicate Stata's `reghdfe` command. Here's how the syntax translates:

**Stata:**
```stata
reghdfe wage experience education, absorb(firm_id year) cluster(firm_id)
```

**Python (reghdfe):**
```python
result = reghdfe(
    data=data,
    y='wage',
    x=['experience', 'education'],
    fe=['firm_id', 'year'],
    cluster=['firm_id']
)
```

## 📋 Key Features

- ✅ **High-dimensional fixed effects** - Efficiently absorb multiple fixed effect dimensions
- ✅ **Cluster-robust standard errors** - Support for one-way and two-way clustering  
- ✅ **Weighted regression** - Handle sampling weights and frequency weights
- ✅ **Singleton dropping** - Automatically handle singleton groups
- ✅ **Fast computation** - Optimized algorithms for large datasets
- ✅ **Stata compatibility** - Results match Stata's reghdfe command

## Integration Options

This package is **actively maintained** as a standalone library. For users who prefer a unified ecosystem with additional econometric and statistical tools, `reghdfe` functionality is also available through:

- **[StatsPAI](https://github.com/brycewang-stanford/StatsPAI/)** - Stats + Econometrics + ML + AI + LLMs

## Related Projects

- **[StatsPAI](https://github.com/brycewang-stanford/StatsPAI/)** - StatsPAI = Stats + Econometrics + ML + AI + LLMs  
- **[PyStataR](https://github.com/brycewang-stanford/PyStataR)** - Unified Stata-equivalent commands and R functions

## Documentation

For detailed API reference and additional examples, visit our [GitHub repository](https://github.com/brycewang-stanford/reghdfe).

## Contributing

We welcome contributions! Please feel free to:
- Report bugs or request features via [GitHub Issues](https://github.com/brycewang-stanford/reghdfe/issues)
- Submit pull requests for improvements
- Share your use cases and examples

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**This package is actively maintained.** For questions, bug reports, or feature requests, please open an issue on [GitHub](https://github.com/brycewang-stanford/pyreghdfe/issues).