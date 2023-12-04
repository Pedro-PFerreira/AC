import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, roc_curve

import matplotlib.pyplot as plt
import seaborn as sns

df_ea = pd.read_csv('../../new_final_dataset_ea.csv')
df_we = pd.read_csv('../../new_final_dataset_we.csv')

columns_to_update = ['playerScore', 'postPlayerScore', 'playerID', 'threeAccuracy', 'postThreeAccuracy', 'bmi']

def update_columns(df):

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

update_columns(df_ea)
update_columns(df_we)

def replace_values(df, column):
    unique_values = df[column].unique()
    value_to_index = {value: idx for idx, value in enumerate(unique_values)}
    df[column] = df[column].replace(value_to_index)

# replace tmID for a number, in order to be used in the classification model
replace_values(df_ea, 'tmID')
replace_values(df_we, 'tmID')

# replace playerID for a number, in order to be used in the classification model
replace_values(df_ea, 'playerID')
replace_values(df_we, 'playerID')

replace_values(df_ea, 'confID')
replace_values(df_we, 'confID')

replace_values(df_ea, 'coachID')
replace_values(df_we, 'coachID')

# store the teamID and the team name in a dictionary
teamID_to_name = df_ea[['tmID', 'name']].drop_duplicates().set_index('tmID').to_dict()['name']
teamID_to_name = df_we[['tmID', 'name']].drop_duplicates().set_index('tmID').to_dict()['name']

df_ea = df_ea.drop(['name', 'stint', 'won', 'lost', 'post_wins', 'post_losses', 'teams_score'], axis=1)
df_we = df_we.drop(['name', 'stint', 'won', 'lost', 'post_wins', 'post_losses', 'teams_score'], axis=1)

# convert playoff, firstRound, semis and finals to boolean

df_ea['playoff'] = df_ea['playoff'].astype('bool')
df_ea['firstRound'] = df_ea['firstRound'].astype('bool')
df_ea['semis'] = df_ea['semis'].astype('bool')
df_ea['finals'] = df_ea['finals'].astype('bool')

df_we['playoff'] = df_we['playoff'].astype('bool')
df_we['firstRound'] = df_we['firstRound'].astype('bool')
df_we['semis'] = df_we['semis'].astype('bool')
df_we['finals'] = df_we['finals'].astype('bool')

# replace missing values with the mean
df_ea = df_ea.fillna(df_ea.mean())
df_we = df_we.fillna(df_ea.mean())

def prediction(df):

    # Define the sliding window size (e.g., 1 year)
    window_size = 2
    accuracies = []

    # Create the model
    model = DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=0)
    
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

prediction(df_ea)
prediction(df_we)

def print_results(df):

    for i in range(1,12):

        playoff_teams = df[df['year'] == i][df['playoff'] == True]['tmID'].values

        # print(playoff_teams)

        # Convert the Ids to the team names

        playoff_teams = [teamID_to_name[team] for team in playoff_teams]

        # Remove duplicate names

        playoff_teams = list(set(playoff_teams))
        print("Year: ", i, "Playoff teams:")
        print(playoff_teams)

print_results(df_ea)
print_results(df_we)