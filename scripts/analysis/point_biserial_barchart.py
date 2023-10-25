import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Load your data
data = pd.read_csv("../../final_dataset.csv", delimiter=";")

# Define the continuous attributes
continuous_attributes = ["playerScore", "postPlayerScore", "threeAccuracy", "postThreeAccuracy", "height", "weight", "won", "W", "teams_score"]
binary_target = data["playoff"]

# Initialize empty lists to store correlation and p-value results
correlation_values = []
p_values = []

# Calculate point-biserial correlation and p-values for each attribute
for attribute in continuous_attributes:
    point_biserial_corr, p_value = stats.pointbiserialr(data[attribute], binary_target)
    correlation_values.append(point_biserial_corr)
    p_values.append(p_value)

# Create a bar chart
plt.figure(figsize=(10, 6))
bars = plt.barh(continuous_attributes, correlation_values, color='skyblue', label='Correlation')
plt.axvline(0, color='black', linestyle='--')
plt.xlabel('Point-biserial Correlation')
plt.title('Point-biserial Correlation for Continuous Attributes')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Add exact correlation values as annotations
for bar, corr_value in zip(bars, correlation_values):
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{corr_value:.2f}', ha='left', va='center')

# Display the chart
plt.show()
