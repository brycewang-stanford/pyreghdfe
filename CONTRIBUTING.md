# Contributing to PyRegHDFE

We welcome contributions to PyRegHDFE! This document provides guidelines for contributing to the project.

## Getting Started

### Setting up the Development Environment

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/pyreghdfe.git
   cd pyreghdfe
   ```

3. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e .[dev]
   ```

4. Run tests to ensure everything is working:
   ```bash
   pytest
   ```

## Development Workflow

### Creating a New Feature

1. Create a new branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes
3. Add tests for new functionality
4. Run the test suite and linting:
   ```bash
   # Run tests
   pytest
   
   # Run linting
   ruff check pyreghdfe/
   ruff format pyreghdfe/
   
   # Type checking
   mypy pyreghdfe/
   ```

5. Commit your changes with a descriptive message
6. Push to your fork and create a pull request

### Code Style

We use [Ruff](https://docs.astral.sh/ruff/) for code formatting and linting. Please ensure your code follows these standards:

- Line length: 88 characters
- Use type hints for all function parameters and return values
- Follow PEP 8 naming conventions
- Add docstrings for all public functions and classes

### Testing

- All new features must include tests
- Tests should cover both typical use cases and edge cases
- Use descriptive test names that explain what is being tested
- Aim for high test coverage

### Documentation

- Update docstrings for any modified functions or classes
- Add examples to docstrings when helpful
- Update the README if you're adding new features
- Consider adding examples to the examples/ directory

## Types of Contributions

### Bug Reports

When reporting bugs, please include:
- Python version and operating system
- PyRegHDFE version
- Minimal code example that reproduces the bug
- Expected behavior vs. actual behavior
- Full error traceback if applicable

### Feature Requests

For feature requests:
- Describe the use case and motivation
- Provide examples of how the feature would be used
- Consider whether it fits with the project's scope and goals

### Code Contributions

We especially welcome contributions in these areas:
- Performance optimizations
- Additional algorithms (e.g., CG, Kaczmarz)
- Enhanced standard error options (HC2, HC3, etc.)
- Better error messages and input validation
- Documentation improvements
- Examples and tutorials

## Project Structure

```
pyreghdfe/
├── pyreghdfe/          # Main package
│   ├── __init__.py
│   ├── api.py          # Public API
│   ├── core.py         # Core estimation logic
│   ├── results.py      # Results class
│   ├── covariance.py   # Standard error calculations
│   └── hdfe.py         # Fixed effects interface
├── tests/              # Test suite
├── README.md
├── LICENSE
└── pyproject.toml
```

## Code Review Process

1. All changes must be reviewed via pull requests
2. At least one maintainer must approve the PR
3. All tests must pass
4. Code style checks must pass
5. Type checking must pass without errors

## Release Process

Releases follow semantic versioning (MAJOR.MINOR.PATCH):
- PATCH: Bug fixes and small improvements
- MINOR: New features, backward compatible
- MAJOR: Breaking changes

## Getting Help

- Open an issue for bugs or feature requests
- Join discussions in existing issues
- Reach out to maintainers for questions about contribution

## Code of Conduct

This project follows a code of conduct to ensure a welcoming environment for all contributors. Please be respectful and inclusive in all interactions.

## Recognition

Contributors will be acknowledged in the CONTRIBUTORS.md file and in release notes.

Thank you for contributing to PyRegHDFE!
