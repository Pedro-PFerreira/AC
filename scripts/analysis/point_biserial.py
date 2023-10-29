import numpy as np
import pandas as pd
from scipy import stats

data = pd.read_csv("../../final_dataset.csv", delimiter=";")

continuous_attributes = ["playerScore", "postPlayerScore", "threeAccuracy", "postThreeAccuracy", "height", "weight", "won", "W", "teams_score"]
binary_target = data["playoff"]

for attribute in continuous_attributes:
    print("Attribute:", attribute)
    point_biserial_corr, p_value = stats.pointbiserialr(data[attribute], binary_target)
    print("Point-biserial correlation:", point_biserial_corr)
    print("P-value:", p_value)
    print()
