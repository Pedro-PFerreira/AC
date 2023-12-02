import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('new_final_dataset_11.csv', delimiter=';')

columns_to_update = ['playerScore', 'postPlayerScore', 'playerID', 'threeAccuracy', 'postThreeAccuracy', 'bmi']

for year in range(11, 1, -1):
    year_data = df[df['year'] == year]
    prev_year_data = df[df['year'] == year - 1]

    # Loop through all rows of the year
    for index, row in year_data.iterrows():
        player = row['playerID']

        if not prev_year_data[prev_year_data['playerID'] == player].empty:
            # Replace selected columns for the current year with the values from the previous year
            for column in columns_to_update:
                df.loc[(df['year'] == year) & (df['playerID'] == player), column] = prev_year_data[prev_year_data['playerID'] == player][column].values[0]
        else:
            # If the player is not found in the previous year, replace selected columns with NaN
            for column in columns_to_update:
                df.loc[(df['year'] == year) & (df['playerID'] == player), column] = np.nan

def replace_values(df, column):
    unique_values = df[column].unique()
    value_to_index = {value: idx for idx, value in enumerate(unique_values)}
    df[column] = df[column].replace(value_to_index)

# replace tmID for a number, in order to be used in the classification model
replace_values(df, 'tmID')

# replace playerID for a number, in order to be used in the classification model
replace_values(df, 'playerID')

replace_values(df, 'confID')

replace_values(df, 'coachID')

# store the teamID and the team name in a dictionary
teamID_to_name = df[['tmID', 'name']].drop_duplicates().set_index('tmID').to_dict()['name']

df = df.drop(['name', 'stint'], axis=1)

# convert playoff, firstRound, semis and finals to boolean

df['playoff'] = df['playoff'].astype('bool')
df['firstRound'] = df['firstRound'].astype('bool')
df['semis'] = df['semis'].astype('bool')
df['finals'] = df['finals'].astype('bool')

# replace missing values with the mean
df = df.fillna(df.mean())

# Define the sliding window size (e.g., 1 year)
window_size = 1
accuracies = []

# Create the model
model = DecisionTreeClassifier()
   
for year in range(2, 12):
    # Select the data for the current year
    current_year_data = df[df['year'] == year]
    
    # Select the data for the previous years as training data
    training_data = df[df['year'].isin(range(year - window_size, year))]
    
    # Split the training and test datasets
    train_features = training_data.drop(['playoff'], axis=1)
    train_label = training_data['playoff']
    test_features = current_year_data.drop(['playoff'], axis=1)
    test_label = current_year_data['playoff']
    
    model.fit(train_features, train_label)
    
    predictions = model.predict(test_features)
    
    # Calculate the accuracy for the current year
    accuracy = np.mean(predictions == test_label)
    accuracies.append(accuracy)
    
    print(f"The accuracy for year {year} is: {accuracy}")

    # Calculate the precision for the current year

    precision = np.mean(predictions[predictions == 1] == test_label[predictions == 1])
    print(f"The precision for year {year} is: {precision}")

    # Calculate the F-measure for the current year

    f_measure = 2 * (precision * accuracy) / (precision + accuracy)

    print(f"The F-measure for year {year} is: {f_measure}")

# Retrive the name of the teams that go to the playoffs in the last year

playoff_teams = df[df['year'] == 11][df['playoff'] == 1]['tmID'].values

print(playoff_teams)

# Convert the Ids to the team names

playoff_teams = [teamID_to_name[team] for team in playoff_teams]

# Remove duplicate names

playoff_teams = list(set(playoff_teams))

print(playoff_teams)