import pandas as pd
from scipy.stats import chi2_contingency
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data loading
data = pd.read_csv("../../final_dataset_before.csv", sep=";")

continuous_attributes = ["playerScore", "postPlayerScore", "threeAccuracy", "postThreeAccuracy", "height", "weight", "won", "W", "teams_score"]
nominal_attributes = ["pos", "award", "playoff", "firstRound", "semis", "finals"]

# Function to compute eta squared
def eta_squared(nominal_col, continuous_col):
    # Create a contingency table
    contingency = pd.crosstab(nominal_col, continuous_col)
    
    # Perform chi2 test
    chi2, _, _, _ = chi2_contingency(contingency)
    
    # Compute eta squared
    return chi2 / (chi2 + len(data))

# Create an empty DataFrame to store eta squared values
correlation_matrix = pd.DataFrame(index=nominal_attributes, columns=continuous_attributes)

# Calculate eta squared for each pair of attributes
for nominal in nominal_attributes:
    for continuous in continuous_attributes:
        correlation_matrix.at[nominal, continuous] = eta_squared(data[nominal], data[continuous])

plt.figure(figsize=(12, 6))
sns.heatmap(correlation_matrix.astype(float), annot=True, cmap='viridis_r', cbar_kws={'label': 'Eta-squared'}, vmin=0, vmax=1)
plt.title("Eta-squared values between categorical and numerical attributes")
plt.show()
