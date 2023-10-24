import pandas as pd
from scipy.stats import spearmanr, chi2_contingency

df = pd.read_csv('final_dataset.csv', delimiter=';')

# Function to compute eta squared
def compute_eta_squared(nominal_col, ordinal_col):
    contingency = pd.crosstab(nominal_col, ordinal_col)
    chi2, _, _, _ = chi2_contingency(contingency)
    return chi2 / (chi2 + len(df))

# Calculate eta-squared for each nominal attribute with 'rank'
nominal_attributes = ['tmID', 'pos', 'award', 'year']
eta_squared_values = {}

for attr in nominal_attributes:
    eta_squared_values[attr] = compute_eta_squared(df[attr], df['rank'])


print(f"The values for the eta squared for each variable compared to the rank are:\n{eta_squared_values}")