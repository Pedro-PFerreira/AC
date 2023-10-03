import pandas as pd

def merge():

    # Retrieve all the cleaned datasets

    df_teams = pd.read_csv('data/cleaned/teams_cleaned.csv')
    df_players_teams = pd.read_csv('data/cleaned/players_teams_reduced.csv')
    df_coaches = pd.read_csv('data/cleaned/coaches.csv')
    df_awards = pd.read_csv('data/cleaned/awards_players.csv')

    # Merge the datasets
    
    

