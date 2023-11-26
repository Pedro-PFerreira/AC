import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("new_final_dataset.csv", sep=";")

continuous_attributes = ["playerScore", "postPlayerScore", "threeAccuracy", "postThreeAccuracy", "bmi", "winRatio", "awards","postWinRatio", "teams_score"]
nominal_attributes = ["playoff"]

for nominal in nominal_attributes:
    for continuous in continuous_attributes:
        plt.figure(figsize=(10, 5))
        sns.boxplot(data=data, x=nominal, y=continuous)
        plt.title(f'Distribution of {continuous} across {nominal}')
        plt.show()