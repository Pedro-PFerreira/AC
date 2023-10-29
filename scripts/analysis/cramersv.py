import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data (use your data here)
data = pd.read_csv("../../data/cleaned/teams_post_cleaned.csv", sep=";")

data = data.drop(["birthDate","deathDate", "bmi"], axis=1)

data = data.dropna()


# Function to compute Cramér's V
def cramers_v(x, y):
    confusion_matrix = pd.crosstab(x, y)
    chi2 = chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k-1)*(r-1))/(n-1))
    rcorr = r - ((r-1)**2)/(n-1)
    kcorr = k - ((k-1)**2)/(n-1)
    return np.sqrt(phi2corr / min((kcorr-1), (rcorr-1)))

# Create a matrix to store the results
attributes = data.columns
correlation_matrix = pd.DataFrame(index=attributes, columns=attributes)

# Compute Cramér's V for each pair of attributes
for attr1 in attributes:
    for attr2 in attributes:
        correlation_matrix.at[attr1, attr2] = cramers_v(data[attr1], data[attr2])

# Visualize using a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix.astype(float), annot=True, cmap='coolwarm', cbar_kws={'label': "Cramér's V"})
plt.title("Nominal Attribute Associations using Cramér's V")
plt.show()