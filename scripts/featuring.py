import pandas as pd
import numpy as np


df_awards = pd.read_csv('data/cleaned/awards_players.csv', delimiter=';')

df_coaches = pd.read_csv('data/cleaned/coaches.csv', delimiter=';') 

df_players = pd.read_csv('data/cleaned/players_cleaned.csv', delimiter=';')

df_players_teams = pd.read_csv('data/cleaned/players_teams_cleaned.csv', delimiter=';')

series_post = pd.read_csv('data/cleaned/series_post_cleaned.csv', delimiter=';')

df_teams = pd.read_csv('data/cleaned/teams_merged.csv')

# Rename ID variables to match the other datasets

df_players.rename(columns={'bioID': 'personID'}, inplace=True)

df_coaches.rename(columns={'coachID': 'personID'}, inplace=True)

df_players_teams.rename(columns={'playerID': 'personID'}, inplace=True)

df_awards.rename(columns={'playerID': 'personID'}, inplace=True)


# merge all the datsets

df1 = df_players.merge(df_awards, how='left', on=['personID'])

# Set 0 for year, in order to remove NaN

df1['year'] = df1['year'].fillna(0)

df1 = df1.merge(df_players_teams, how='left', on=['personID'])

#print(df1.head())

df2 = df_coaches.merge(df_awards, how='left', on=['personID', 'year'])

#print(df2.head())

df3 = pd.concat([df1, df2])
df3['year'] = df3['year'].fillna(0)

print(df3.head())

# # write to a new csv

df3.to_csv('data/cleaned/merged_dataset_cleaned.csv', index=False)
