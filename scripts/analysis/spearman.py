import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

# Sample data loading
data = pd.read_csv("new_final_dataset.csv", sep=";")

# Categorical variable (nominal)
categorical_variables = ["awards", "playoff", "firstRound", "semis", "finals"]

# Ordinal variable
ordinal_variable = data['rank']

# Create an empty DataFrame to store the correlation results
correlation_results = pd.DataFrame(index=categorical_variables, columns=['Correlation'])

# Calculate the Spearman correlation for each categorical variable
for categorical_attribute in categorical_variables:
    categorical_variable_rank = data[categorical_attribute].rank()
    correlation, p_value = spearmanr(categorical_variable_rank, ordinal_variable)
    correlation_results.at[categorical_attribute, 'Correlation'] = correlation

# Convert the 'Correlation' column to float type
correlation_results['Correlation'] = correlation_results['Correlation'].astype(float)

# Create a heatmap to visualize the correlations
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_results, annot=True, cmap='coolwarm', cbar_kws={'label': 'Spearman Correlation'})
plt.title("Spearman Correlation Heatmap")
plt.show()