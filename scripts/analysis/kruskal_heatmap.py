import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Sample data loading
data = pd.read_csv("../../new_final_dataset.csv", sep=";")

# continuous_attributes = ["winRatio", "teams_score"]
ordinal_attributes = ["rank"]
nominal_attributes = ["pos", "awards", "playoff", "firstRound", "semis", "finals"]

# Create dummy variables for nominal attributes
dummy_vars = pd.get_dummies(data[nominal_attributes], drop_first=True)


# Combine the dummy variables with the continuous attributes
# data_with_dummies = pd.concat([data[continuous_attributes], dummy_vars], axis=1)
data_with_dummies = pd.concat([data[ordinal_attributes], dummy_vars], axis=1)

# Dictionary to hold results
results = {}

for dummy_attribute in dummy_vars.columns:
    results[dummy_attribute] = {}
    # for attribute in continuous_attributes:
    for attribute in ordinal_attributes:
        h_statistic, p_value = stats.kruskal(data_with_dummies[attribute][data_with_dummies[dummy_attribute] == 1],
                                             data_with_dummies[attribute][data_with_dummies[dummy_attribute] == 0])
        results[dummy_attribute][attribute + '_H'] = h_statistic
        results[dummy_attribute][attribute + '_P'] = p_value

# Convert the results dictionary to a DataFrame
df_results = pd.DataFrame.from_dict(results, orient='index')

# Separate out H-statistics and P-values
h_values = df_results[[col for col in df_results.columns if '_H' in col]]
p_values = df_results[[col for col in df_results.columns if '_P' in col]]

# Plot heatmaps

# Adjust pandas display settings
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# Function to format annotations
def format_heatmap_annotations(val):
    if isinstance(val, float):
        return f"{val:.5f}"
    return val

# Plot heatmaps

# H-statistics heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(h_values, annot=True, cmap='coolwarm', cbar_kws={'label': 'H-statistic'}, fmt=".5f")
plt.title("H-statistics from Kruskal-Wallis test")
plt.show()

# P-values heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(p_values, annot=True, cmap='viridis_r', cbar_kws={'label': 'P-value'}, vmin=0, vmax=1, fmt=".5f")
plt.title("P-values from Kruskal-Wallis test")
plt.show()