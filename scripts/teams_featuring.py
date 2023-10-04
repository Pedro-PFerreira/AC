import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Load the dataset

df = pd.read_csv('data/cleaned/teams_merged.csv')

# See the correlation matrix between the features

corr = df.corr()

# Plot the correlation matrix between the features

plt.figure(figsize=(10, 8))  # Set the figure size
sb.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.show()

# Drop the columns that are highly correlated to each other

df = df.drop(['o_fga','o_3pm','o_3pa','o_dreb','o_reb'], axis=1)

df = df.drop(['d_pts', 'd_fgm', 'd_dreb', 
              'd_fta', 'd_ftm', 'd_oreb',
              'd_stl', 'd_asts', 'd_blk',
              'd_pf', 'd_to', 'd_3pa',
              'd_reb', 'd_fga', 'd_3pm'], axis=1)

df = df.drop('GP', axis=1)

# Plot the correlation matrix between the features

new_corr = df.corr()
plt.figure(figsize=(10, 8))  # Set the figure size
sb.heatmap(new_corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.show()