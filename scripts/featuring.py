import pandas as pd
import numpy as np


def featuring(df):

    df_awards = pd.read_csv('../data/cleaned/awards_players.csv')

    df_coaches = pd.read_csv('../data/cleaned/coaches.csv') 

    df_players_teams = pd.read_csv('../data/cleaned/players_teams_reduced.csv')

    series_post = pd.read_csv('../data/cleaned/series_post_cleaned.csv')

    df_teams = pd.read_csv('../data/cleaned/teams_merged.csv')
    