import pandas as pd

def cleaning_teams():

    df = pd.read_csv('data/raw/teams.csv')

    # drop irrelevant columns, such as franchID, condID, divID, seeded, etc.

    df = df.drop(['lgID', 'franchID', 'confID', 'divID', 'seeded'], axis=1)

    # drop columns that leads to data leakage (i.e. data that should not available at the time of prediction)

    df = df.drop(['firstRound', 'semis', 'finals'], axis=1)

    # drop columns that have invalid data

    df = df.drop(['tmORB', 'tmDRB','tmTRB', 'opptmORB', 'opptmDRB', 'opptmTRB'], axis=1)


    print(df.head())


cleaning_teams()