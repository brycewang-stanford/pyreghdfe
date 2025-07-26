# Changelog

All notable changes to PyRegHDFE will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-01-25

### Added
- Initial release of PyRegHDFE
- Multi-dimensional fixed effects regression (up to 5+ dimensions)
- Multiple absorption algorithms:
  - Within transform for single fixed effects
  - Method of Alternating Projections (MAP) for multiple fixed effects
  - LSMR sparse solver for high-dimensional problems
- Robust standard errors (HC1)
- Cluster-robust standard errors (1-way and 2-way clustering)
- Weighted regression with analytic weights
- Comprehensive regression diagnostics:
  - R-squared (overall and within)
  - F-statistics
  - Confidence intervals
  - Standard errors, t-values, p-values
- Stata-like API and output formatting
- Automatic singleton dropping
- Full test suite with extensive coverage
- Complete documentation and examples

### Performance
- Efficient handling of large datasets (100K+ observations)
- Memory-optimized algorithms for high-dimensional fixed effects
- Comparable performance to Stata's reghdfe

### API
- `reghdfe()` main estimation function
- `RegressionResults` class with comprehensive output
- Type hints throughout the codebase
- Pandas-native interface

## [Unreleased]

### Planned for v0.2.0
- Heterogeneous slopes (group-specific coefficients)
- Parallel processing support
- Enhanced prediction functionality
- Additional robust standard error types (HC2, HC3)
- Performance optimizations

### Planned for v0.3.0
- Group-level results (`group()` equivalent)
- Individual fixed effects control (`individual()` equivalent)
- Save fixed effects estimates (`savefe` equivalent)
- Advanced diagnostics and testing

### Planned for v1.0.0
- Full feature parity with Stata reghdfe
- Enterprise-grade stability and performance
- Comprehensive documentation and tutorials
- Integration with popular econometrics packages
