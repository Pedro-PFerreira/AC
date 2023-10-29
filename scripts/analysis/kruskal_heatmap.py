import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Sample data loading
data = pd.read_csv("../../final_dataset.csv", sep=";")

continuous_attributes = ["playerScore", "postPlayerScore", "threeAccuracy", "postThreeAccuracy", "height", "weight", "won", "W", "teams_score"]
nominal_attributes = ["pos", "award", "playoff", "firstRound", "semis", "finals"]

# Dictionary to hold results
results = {}

for nominal_attribute in nominal_attributes:
    results[nominal_attribute] = {}
    for attribute in continuous_attributes:
        groups = [data[attribute][data[nominal_attribute] == category] for category in np.unique(data[nominal_attribute])]
        
        h_statistic, p_value = stats.kruskal(*groups)
        
        results[nominal_attribute][attribute + '_H'] = h_statistic
        results[nominal_attribute][attribute + '_P'] = p_value

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