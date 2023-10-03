import pandas as pd

def cleanTeams():

    df = pd.read_csv('data/raw/teams.csv')

    # drop irrelevant columns, such as franchID, condID, divID, seeded, etc.

    df = df.drop(['lgID', 'franchID', 'confID', 'divID', 'seeded'], axis=1)

    # drop columns that have invalid data

    df = df.drop(['tmORB', 'tmDRB','tmTRB', 'opptmORB', 'opptmDRB', 'opptmTRB'], axis=1)

    # write to csv

    df.to_csv('data/cleaned/teams_cleaned.csv', index=False)

def cleanTeamsPost():

    df = pd.read_csv('data/raw/teams_post.csv')

    # drop lgID, since its irrelevant

    df = df.drop(['lgID'], axis=1)

    # write to csv

    df.to_csv('data/cleaned/teams_post_cleaned.csv', index=False)

def mergeTeams():

    # retrieve all the cleaned datasets related to teams

    df_teams = pd.read_csv('data/cleaned/teams_cleaned.csv')
    df_teams_post = pd.read_csv('data/cleaned/teams_post_cleaned.csv')

    # merge the datasets

    df_teams = df_teams.merge(df_teams_post, how='left', on=['year', 'tmID'])

    # drop redundant columns- won and lost give the same information
    # as confW and confL + W + L. Also, L = number of games - W
    df_teams = df_teams.drop(['won', 'lost', 'confW', 'confL', 'awayL','L'], axis=1)
    
    # write to csv
    df_teams.to_csv('data/cleaned/teams_merged.csv', index=False)

cleanTeams()
cleanTeamsPost()
mergeTeams()


