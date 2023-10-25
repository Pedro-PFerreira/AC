import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

data = pd.read_csv("../../final_dataset.csv", sep=";")

continuous_attributes = ["playerScore", "postPlayerScore", "threeAccuracy", "postThreeAccuracy", "height", "weight", "won", "W", "teams_score"]

ordinal_attribute = data["rank"]

jt_results = {}

for attribute in continuous_attributes:
    jt_statistic, p_value = stats.kendalltau(ordinal_attribute, data[attribute])
    jt_results[attribute] = {"Jonckheere-Terpstra statistic": jt_statistic, "P-value": p_value}

# Extract the statistics and p-values
jt_statistics = [result["Jonckheere-Terpstra statistic"] for result in jt_results.values()]
p_values = [result["P-value"] for result in jt_results.values()]

# Create a bar chart
plt.figure(figsize=(10, 6))
bars = plt.barh(continuous_attributes, jt_statistics, color='skyblue', label='Jonckheere-Terpstra Statistic')
plt.axvline(0, color='black', linestyle='--')
plt.xlabel('Jonckheere-Terpstra Statistic')
plt.title('Jonckheere-Terpstra Statistic for Continuous Attributes')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Add exact Jonckheere-Terpstra statistics as annotations
for bar, stat_value in zip(bars, jt_statistics):
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{stat_value:.2f}', ha='left', va='center')

# Display the chart
plt.show()
