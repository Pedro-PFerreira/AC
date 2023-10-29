import numpy as np
import pandas as pd
from scipy import stats

data = pd.read_csv("../../final_dataset.csv", sep=";")

continuous_attributes = ["playerScore", "postPlayerScore", "threeAccuracy", "postThreeAccuracy", "height", "weight", "won", "W", "teams_score"]
nominal_attributes = ["pos", "award", "playoff", "firstRound", "semis", "finals"]

for nominal_attribute in nominal_attributes:
    print("Nominal attribute:", nominal_attribute)
    for attribute in continuous_attributes:
        groups = [data[attribute][data[nominal_attribute] == category] for category in np.unique(data[nominal_attribute])]
        
        h_statistic, p_value = stats.kruskal(*groups)
        
        print(" Attribute:", attribute)
        print(" H-statistic:", h_statistic)
        print(" P-value:", p_value)
        print()
