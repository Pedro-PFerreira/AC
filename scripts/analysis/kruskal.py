import numpy as np
import pandas as pd
from scipy import stats


# Sample data loading
data = pd.read_csv("../../new_final_dataset.csv", sep=";")

continuous_attributes = ["playerScore", "postPlayerScore", "threeAccuracy", "postThreeAccuracy", "bmi", "winRatio", "postWinRatio", "teams_score"]
nominal_attributes = ["pos", "awards", "playoff", "firstRound", "semis", "finals"]

# Create dummy variables for nominal attributes
dummy_vars = pd.get_dummies(data[nominal_attributes], drop_first=True)  # drop_first=True to avoid multicollinearity

# Combine the dummy variables with the continuous attributes
data_with_dummies = pd.concat([data[continuous_attributes], dummy_vars], axis=1)

# Perform Kruskal-Wallis tests
for dummy_column in dummy_vars.columns:
    print("Dummy attribute:", dummy_column)
    for attribute in continuous_attributes:
        h_statistic, p_value = stats.kruskal(data_with_dummies[data_with_dummies[dummy_column] == 1][attribute],
                                            data_with_dummies[data_with_dummies[dummy_column] == 0][attribute])
        print(" Attribute:", attribute)
        print(" H-statistic:", h_statistic)
        print(" P-value:", p_value)
        print()
