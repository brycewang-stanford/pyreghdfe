"""
Basic PyRegHDFE Examples

This script demonstrates the core functionality of PyRegHDFE with simple examples.
"""

import numpy as np
import pandas as pd
from pyreghdfe import reghdfe

# Set random seed for reproducibility
np.random.seed(42)

print("=" * 60)
print("PyRegHDFE Examples")
print("=" * 60)

# Example 1: Simple OLS (No Fixed Effects)
print("\n1. Simple OLS Regression")
print("-" * 30)

n = 1000
data = pd.DataFrame({
    'y': np.random.normal(0, 1, n),
    'x1': np.random.normal(0, 1, n),
    'x2': np.random.normal(0, 1, n)
})

# Add true relationship: y = 1.0 + 0.5*x1 - 0.3*x2 + error
data['y'] = 1.0 + 0.5 * data['x1'] - 0.3 * data['x2'] + np.random.normal(0, 0.5, n)

# Estimate
results_ols = reghdfe(data=data, y='y', x=['x1', 'x2'])
print(results_ols.summary())

# Example 2: Single Fixed Effect
print("\n2. Single Fixed Effect (Firm FE)")
print("-" * 30)

n_firms = 50
n_obs = 500
data_fe = pd.DataFrame({
    'firm_id': np.random.randint(0, n_firms, n_obs),
    'x': np.random.normal(0, 1, n_obs)
})

# Add firm fixed effects
firm_effects = np.random.normal(0, 1, n_firms)
data_fe['firm_fe'] = data_fe['firm_id'].map(dict(enumerate(firm_effects)))
data_fe['y'] = data_fe['firm_fe'] + 0.8 * data_fe['x'] + np.random.normal(0, 0.3, n_obs)

# Estimate with firm fixed effects
results_fe = reghdfe(data=data_fe, y='y', x='x', fe='firm_id')
print(results_fe.summary())
print(f"True coefficient: 0.8, Estimated: {results_fe.params['x']:.3f}")

# Example 3: Two-Way Fixed Effects
print("\n3. Two-Way Fixed Effects (Firm + Year)")
print("-" * 30)

n_firms, n_years = 30, 8
n_obs = n_firms * n_years

data_2way = pd.DataFrame({
    'firm_id': np.repeat(range(n_firms), n_years),
    'year': np.tile(range(n_years), n_firms),
    'x': np.random.normal(0, 1, n_obs)
})

# Add firm and year fixed effects
firm_effects = np.random.normal(0, 1, n_firms)
year_effects = np.random.normal(0, 0.5, n_years)

data_2way['firm_fe'] = data_2way['firm_id'].map(dict(enumerate(firm_effects)))
data_2way['year_fe'] = data_2way['year'].map(dict(enumerate(year_effects)))
data_2way['y'] = (data_2way['firm_fe'] + data_2way['year_fe'] + 
                  0.6 * data_2way['x'] + np.random.normal(0, 0.2, n_obs))

# Estimate with two-way fixed effects
results_2way = reghdfe(data=data_2way, y='y', x='x', fe=['firm_id', 'year'])
print(results_2way.summary())
print(f"True coefficient: 0.6, Estimated: {results_2way.params['x']:.3f}")

# Example 4: Cluster-Robust Standard Errors
print("\n4. Cluster-Robust Standard Errors")
print("-" * 30)

n_clusters = 20
cluster_size = 25
n_obs = n_clusters * cluster_size

data_cluster = pd.DataFrame({
    'cluster_id': np.repeat(range(n_clusters), cluster_size),
    'x': np.random.normal(0, 1, n_obs)
})

# Add cluster effects
cluster_effects = np.random.normal(0, 0.8, n_clusters)
data_cluster['cluster_effect'] = data_cluster['cluster_id'].map(dict(enumerate(cluster_effects)))
data_cluster['y'] = (0.5 * data_cluster['x'] + data_cluster['cluster_effect'] + 
                     np.random.normal(0, 0.3, n_obs))

# Estimate with cluster-robust standard errors
results_cluster = reghdfe(
    data=data_cluster,
    y='y',
    x='x',
    cluster='cluster_id',
    cov_type='cluster'
)
print(results_cluster.summary())

# Example 5: Weighted Regression
print("\n5. Weighted Regression")
print("-" * 30)

n = 400
data_weight = pd.DataFrame({
    'x': np.random.normal(0, 1, n),
    'weight': np.random.uniform(0.5, 2.0, n)
})

# Create heteroskedastic errors
error_var = 1 + data_weight['x']**2
data_weight['y'] = 0.7 * data_weight['x'] + np.random.normal(0, np.sqrt(error_var))

# Estimate with weights
results_weighted = reghdfe(
    data=data_weight,
    y='y',
    x='x',
    weights='weight'
)
print(results_weighted.summary())

print("\n" + "=" * 60)
print("All examples completed successfully!")
print("=" * 60)
