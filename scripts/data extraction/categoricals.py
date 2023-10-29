import pandas as pd

def extract_categoricals():
    
    awards_teams = pd.read_csv('./data/cleaned/awards_players.csv', delimiter=';')
    coaches = pd.read_csv('./data/cleaned/coaches.csv', delimiter=';')
    teams = pd.read_csv('./data/cleaned/teams_cleaned.csv', delimiter=';')
    players = pd.read_csv('./data/cleaned/players_cleaned.csv', delimiter=';')
    players_teams = pd.read_csv('./data/cleaned/players_teams_cleaned.csv', delimiter=';')
    series_post = pd.read_csv('./data/cleaned/series_post_cleaned.csv', delimiter=';')

    # Extract the categorical features from the awards_players dataset

    awards_teams = awards_teams.drop(["year"], axis=1)

    # Extract the categorical features from the coaches dataset

    coaches = coaches.drop(["year", "won", "lost", "post_wins", "post_losses"], axis=1)

    # Extract the categorical features from the teams dataset

    teams = teams.drop(["year", "rank", "won", "GP", "home", "awayW", "confW", "teams_score", "W", "L"],
                       axis=1)

    # Extract the categorical features from the players dataset

    players = players.drop(["birthDate", "deathDate", "bmi"], axis=1)

    # Extract the categorical features from the players_teams dataset

    players_teams = players_teams.drop(["playerScore", "postPlayerScore", "year", "lgID", "dq",
                                         "postDQ", "threeAccuracy", "postThreeAccuracy",
                                         "post_wins", "post_losses"], axis=1)
    
    # Extract the categorical features from the series_post dataset

    series_post = series_post.drop(["year","W", "L"], axis=1)