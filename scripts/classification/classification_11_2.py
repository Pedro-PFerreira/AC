import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from collections import defaultdict

df_ea = pd.read_csv('../../new_final_dataset_ea.csv', delimiter=';')
df_we = pd.read_csv('../../new_final_dataset_we.csv', delimiter=';')

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
teamID_to_name_ea = df_ea[['tmID', 'name']].drop_duplicates().set_index('tmID').to_dict()['name']
teamID_to_name_we = df_we[['tmID', 'name']].drop_duplicates().set_index('tmID').to_dict()['name']

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

def prediction(df, conf):
    # Define the sliding window size (e.g., 1 year)
    window_size = 2

    # Create the model
    model = DecisionTreeClassifier(criterion='gini', max_depth=3)

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

        # Predict probabilities instead of binary predictions
        probabilities = model.predict_proba(test_features)[:, 1]

        # Apply threshold to convert probabilities to binary predictions (0 or 1)
        threshold = 0.6
        binary_predictions = (probabilities > threshold).astype(int)

        # Calculate the accuracy for the current year
        accuracy = np.mean(binary_predictions == test_label)
        print(f"The accuracy for year {year} is: {accuracy}")

        # ... (Your existing evaluation metrics)

        # Create a DataFrame to store aggregated probabilities for each team
        team_probabilities = pd.DataFrame({
            'tmID': current_year_data['tmID'].unique(),
            'probability': 0.0  # Initial placeholder value
        })

        # Update the aggregated probabilities for each team
        for idx, team_id in enumerate(team_probabilities['tmID']):
            team_probabilities.loc[idx, 'probability'] = np.mean(probabilities[current_year_data['tmID'] == team_id])

        # Select the top 4 teams for each conference based on aggregated probabilities
        top_teams = team_probabilities.nlargest(4, 'probability')['tmID'].values

        if conf == 'ea':
            # Convert the Ids to the team names
            conference_teams = [teamID_to_name_ea[team] for team in top_teams]
        else:
            # Convert the Ids to the team names
            conference_teams = [teamID_to_name_we[team] for team in top_teams]

        # Print the top teams for each conference
        print(f"Year: {year}, Top 4 Teams: {conference_teams}")

# ... (Your existing code)

# Uncomment the following lines to run the modified code
print('Eastern Conference:')
prediction(df_ea, 'ea')
print('Western Conference:')
prediction(df_we, 'we')