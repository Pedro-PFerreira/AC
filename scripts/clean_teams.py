import pandas as pd

df = pd.read_csv('data/raw/teams.csv')

unique_teams = df['tmID'].unique()

unique_teams.sort()

teams_dict = {}

for i in range(len(unique_teams)):
    teams_dict[unique_teams[i]] = i


def cleanTeams():

    df = pd.read_csv('data/raw/teams.csv')

    # drop irrelevant columns, such as franchID, condID, divID, seeded, etc.

    df = df.drop(['lgID', 'franchID', 'confID', 'divID', 'seeded', 'name', 'arena'], axis=1)

    # drop columns that have invalid data

    df = df.drop(['tmORB', 'tmDRB','tmTRB', 'opptmORB', 'opptmDRB', 'opptmTRB'], axis=1)

    # make the playoffs-related data of a year be part of the next one

    df['playoff'] = df['playoff'].shift(1)
    df['firstRound'] = df['firstRound'].shift(1)
    df['semis'] = df['semis'].shift(1)
    df['finals'] = df['finals'].shift(1)
    
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
    df_teams = df_teams.drop(['L', 'confW', 'confL', 'awayL','won', 'lost'], axis=1)

    # insert a new column, in order to extract better information about the team's performance

    df_teams['teams_score'] = df_teams['o_pts'] + 0.4 * df_teams['o_fgm'] -0.7*df_teams['o_fta'] -0.4 * (df_teams['o_fta']-df_teams['o_ftm'])+0.7 * df_teams['o_oreb']+0.3 * df_teams['o_oreb']+df_teams['o_stl']+ 0.7 * df_teams['o_asts']+0.7* df_teams['o_blk']-0.4 * df_teams['o_pf']- df_teams['o_to']

    # dropped columns that are correlated to the new column

    df_teams = df_teams.drop(['o_fgm','o_fga','o_ftm','o_fta','o_3pm','o_3pa',
                             'o_oreb','o_dreb','o_reb','o_asts','o_pf','o_stl',
                             'o_to','o_blk','o_pts','d_fgm','d_fga','d_ftm','d_fta',
                             'd_3pm','d_3pa','d_oreb','d_dreb','d_reb','d_asts',
                             'd_pf','d_stl','d_to','d_blk','d_pts'], axis=1)

    # convert the binary attributes to 0 and 1, so that we can use them in the correlation matrix

    df_teams['playoff'] = df_teams['playoff'].apply(lambda x: 1 if x == 'Y' else 0)

    df_teams['firstRound'] = df_teams['firstRound'].apply(lambda x: 1 if x == 'Y' else 0)

    df_teams['semis'] = df_teams['semis'].apply(lambda x: 1 if x == 'Y' else 0)

    df_teams['finals'] = df_teams['finals'].apply(lambda x: 1 if x == 'Y' else 0)

    # order the columns by year

    df_teams = df_teams.sort_values(by=['year'])

    # convert the team IDs to numbers

    df_teams['tmID'] = df_teams['tmID'].apply(lambda x: teams_dict[x])

    # write to csv
    df_teams.to_csv('data/cleaned/teams_merged.csv', index=False)

cleanTeams()
cleanTeamsPost()
mergeTeams()