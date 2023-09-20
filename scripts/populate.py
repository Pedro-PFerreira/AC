import pandas as pd

# Read the CSV file
awards_players = pd.read_csv('../data/awards_players.csv')
players_teams = pd.read_csv('../data/players_teams.csv')
players = pd.read_csv('../data/players.csv')
series_post = pd.read_csv('../data/series_post.csv')
teams = pd.read_csv('../data/teams.csv')

# Convert the CSV files to SQL
path = "../db/database.sql"
test_path = "../db/test.sql"

def populate_teams_post(file_path):

    columns = ["year", "tmID", "lgID", "W", "L"]

    teams_post = pd.read_csv('../data/teams_post.csv', usecols=columns)

    f = open(file_path, "a")

    for i in range(len(teams_post.get('year'))):
        f.write("INSERT INTO teams_post(year, tmID, lgID, W, L) VALUES('{year}','{tmID}','{lgID}','{W}','{L}');\n".format(
            year=teams_post.get('year')[i],
            tmID=teams_post.get('tmID')[i],
            lgID=teams_post.get('lgID')[i],
            W=teams_post.get('W')[i],
            L=teams_post.get('L')[i]
        ))

    f.close()

def populate_coaches(file_path):

    columns = ["coachID", "year", "tmID","lgID", "stint", "won", "lost", "post_wins","post_losses"]

    coaches = pd.read_csv('../data/coaches.csv', usecols=columns)

    f = open(file_path, "a")

    for i in range(len(coaches.get('coachID'))):

        f.write("INSERT INTO coaches(coachID, year, tmID, lgID, stint, won, lost, post_wins, post_losses) VALUES('{coachID}','{year}','{tmID}','{lgID}','{stint}','{won}','{lost}','{post_wins}','{post_losses}');\n".format(
            coachID=coaches.get('coachID')[i],
            year=coaches.get('year')[i],
            tmID=coaches.get('tmID')[i],
            lgID=coaches.get('lgID')[i],
            stint=coaches.get('stint')[i],
            won=coaches.get('won')[i],
            lost=coaches.get('lost')[i],
            post_wins=coaches.get('post_wins')[i],
            post_losses=coaches.get('post_losses')[i]
        ))

    f.close()


def populate_teams(file_path):
    colums = ["year", "lgID", "tmID", "franchID",
               "confID", "divID", "rank",
               "playoff", "seeded", "firstRound",
               "semis", "finals", "name", "o_fgm",
               "o_fga", "o_ftm", "o_fta", "o_3pm",
               "o_3pa", "o_oreb", "o_dreb",
               "o_reb", "o_asts", "o_pf", 
               "o_stl", "o_to", "o_blk", 
               "o_pts", "d_fgm", "d_fga"]
    
    teams = pd.read_csv('../data/teams.csv', usecols=colums)

    f = open(file_path, "a")

    for i in range(len(teams.get('year'))):

        f.write("INSERT INTO teams(year, lgID, tmID, franchID, confID, divID, rank, playoff, seeded, firstRound, semis, finals, name, o_fgm, o_fga, o_ftm, o_fta, o_3pm, o_3pa, o_oreb, o_dreb, o_reb, o_asts, o_pf, o_stl, o_to, o_blk, o_pts, d_fgm, d_fga) VALUES('{year}','{lgID}','{tmID}','{franchID}','{confID}','{divID}','{rank}','{playoff}','{seeded}','{firstRound}','{semis}','{finals}','{name}','{o_fgm}','{o_fga}','{o_ftm}','{o_fta}','{o_3pm}','{o_3pa}','{o_oreb}','{o_dreb}','{o_reb}','{o_asts}','{o_pf}','{o_stl}','{o_to}','{o_blk}','{o_pts}','{d_fgm}','{d_fga}');\n".format(

            year=teams.get('year')[i],
            lgID=teams.get('lgID')[i],
            tmID=teams.get('tmID')[i],
            franchID=teams.get('franchID')[i],
            confID=teams.get('confID')[i],
            divID=teams.get('divID')[i],
            rank=teams.get('rank')[i],
            playoff=teams.get('playoff')[i],
            seeded=teams.get('seeded')[i],
            firstRound=teams.get('firstRound')[i],
            semis=teams.get('semis')[i],
            finals=teams.get('finals')[i],
            name=teams.get('name')[i],
            o_fgm=teams.get('o_fgm')[i],
            o_fga=teams.get('o_fga')[i],
            o_ftm=teams.get('o_ftm')[i],
            o_fta=teams.get('o_fta')[i],
            o_3pm=teams.get('o_3pm')[i],
            o_3pa=teams.get('o_3pa')[i],
            o_oreb=teams.get('o_oreb')[i],
            o_dreb=teams.get('o_dreb')[i],
            o_reb=teams.get('o_reb')[i],
            o_asts=teams.get('o_asts')[i],
            o_pf=teams.get('o_pf')[i],
            o_stl=teams.get('o_stl')[i],
            o_to=teams.get('o_to')[i],
            o_blk=teams.get('o_blk')[i],
            o_pts=teams.get('o_pts')[i],
            d_fgm=teams.get('d_fgm')[i],
            d_fga=teams.get('d_fga')[i]
        ))

    f.close()



#populate_teams_post(test_path)
#populate_coaches(test_path)









#convert_to_sql(test_path, awards_players)