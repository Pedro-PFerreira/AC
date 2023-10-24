import pandas as pd
from scipy import stats

data = pd.read_csv("../../final_dataset.csv", sep=";")

continuous_attributes = ["playerScore", "postPlayerScore", "threeAccuracy", "postThreeAccuracy", "height", "weight", "won", "W", "teams_score"]

ordinal_attribute = data["rank"]

jt_results = {}

for attribute in continuous_attributes:
    jt_statistic, p_value = stats.kendalltau(ordinal_attribute, data[attribute])

    jt_results[attribute] = {"Jonckheere-Terpstra statistic": jt_statistic, "P-value": p_value}

for attribute, result in jt_results.items():
    print("Attribute:", attribute)
    print("Jonckheere-Terpstra statistic:", result["Jonckheere-Terpstra statistic"])
    print("P-value:", result["P-value"])
    print()
