import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

data = pd.read_csv("new_final_dataset.csv", delimiter=";")

continuous_attributes = ["playerScore", "postPlayerScore", "threeAccuracy", "postThreeAccuracy", "bmi", "winRatio", "postWinRatio","teams_score"]
categoricals_attributes = ["awards", "playoff", "firstRound", "semis", "finals"]
correlation_values = []

# Create a dictionary to map attributes to their corresponding correlation values
correlation_dict = {attr: [] for attr in continuous_attributes}

for attribute in continuous_attributes:
    for cat_attribute in categoricals_attributes:
        # Check and handle missing values
        valid_data = data.dropna(subset=[attribute, cat_attribute])

        if len(valid_data) > 0:
            point_biserial_corr, _ = stats.pointbiserialr(valid_data[attribute], valid_data[cat_attribute])
            correlation_dict[attribute].append(point_biserial_corr)
        else:
            correlation_dict[attribute].append(np.nan)

plt.figure(figsize=(10, 6))

# Filter continuous attributes that have corresponding correlation values
filtered_continuous_attributes = [attr for attr in continuous_attributes if len(correlation_dict[attr]) > 0]

bars = plt.barh(filtered_continuous_attributes, [max(correlation_dict[attr]) for attr in filtered_continuous_attributes], color='skyblue', label='Correlation')
plt.axvline(0, color='black', linestyle='--')
plt.xlabel('Point-biserial Correlation')
plt.title('Point-biserial Correlation for Continuous Attributes')
plt.grid(axis='x', linestyle='--', alpha=0.7)

for bar, attr in zip(bars, filtered_continuous_attributes):
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{max(correlation_dict[attr]):.2f}', ha='left', va='center')

plt.show()