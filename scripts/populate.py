import pandas as pd

# Read the CSV file
awards_players = pd.read_csv('../data/awards_players.csv')

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

def populate_series_post(file_path):

    columns = ["year", "round", "series",
               "tmIDWinner", "lgIDWinner",
               "tmIDLoser", "lgIDLoser",
                "W", "L"]
    
    series_post = pd.read_csv('../data/series_post.csv', usecols=columns)

    f = open(file_path, "a")

    for i in range(len(series_post.get('year'))):

        f.write("INSERT INTO series_post(year, round, series, tmIDWinner, lgIDWinner, tmIDLoser, lgIDLoser, W, L) VALUES('{year}','{round}','{series}','{tmIDWinner}','{lgIDWinner}','{tmIDLoser}','{lgIDLoser}','{W}','{L}');\n".format(

            year=series_post.get('year')[i],
            round=series_post.get('round')[i],
            series=series_post.get('series')[i],
            tmIDWinner=series_post.get('tmIDWinner')[i],
            lgIDWinner=series_post.get('lgIDWinner')[i],
            tmIDLoser=series_post.get('tmIDLoser')[i],
            lgIDLoser=series_post.get('lgIDLoser')[i],
            W=series_post.get('W')[i],
            L=series_post.get('L')[i]
        ))

    f.close()


def populate_players_teams(file_path):

    columns = ["playerID", "year", "stint",
              "tmID", "lgID", "GP", "GS",
              "minutes", "points", "oRebounds",
              "dRebounds", "rebounds", "assists",
              "steals", "blocks", "turnovers",
              "PF", "fgAttempted", "fgMade",
              "ftAttempted", "ftMade", "threeAttempted",
              "threeMade", "dq","PostGP",
              "PostGS", "PostMinutes",
              "PostPoints", "PostoRebounds",
              "PostdRebounds"
              ]
    
    players_teams = pd.read_csv('../data/players_teams.csv', usecols=columns)

    f = open(file_path, "a")

    for i in range(len(players_teams.get('playerID'))):

        f.write("INSERT INTO players_teams(playerID, year, stint, tmID, lgID, GP, GS, minutes, points, oRebounds, dRebounds, rebounds, assists, steals, blocks, turnovers, PF, fgAttempted, fgMade, ftAttempted, ftMade, threeAttempted, threeMade, dq, PostGP, PostGS, PostMinutes, PostPoints, PostoRebounds, PostdRebounds) VALUES('{playerID}','{year}','{stint}','{tmID}','{lgID}','{GP}','{GS}','{minutes}','{points}','{oRebounds}','{dRebounds}','{rebounds}','{assists}','{steals}','{blocks}','{turnovers}','{PF}','{fgAttempted}','{fgMade}','{ftAttempted}','{ftMade}','{threeAttempted}','{threeMade}','{dq}','{PostGP}','{PostGS}','{PostMinutes}','{PostPoints}','{PostoRebounds}','{PostdRebounds}');\n".format(
            playerID=players_teams.get('playerID')[i],
            year=players_teams.get('year')[i],
            stint=players_teams.get('stint')[i],
            tmID=players_teams.get('tmID')[i],
            lgID=players_teams.get('lgID')[i],
            GP=players_teams.get('GP')[i],
            GS=players_teams.get('GS')[i],
            minutes=players_teams.get('minutes')[i],
            points=players_teams.get('points')[i],
            oRebounds=players_teams.get('oRebounds')[i],
            dRebounds=players_teams.get('dRebounds')[i],
            rebounds=players_teams.get('rebounds')[i],
            assists=players_teams.get('assists')[i],
            steals=players_teams.get('steals')[i],
            blocks=players_teams.get('blocks')[i],
            turnovers=players_teams.get('turnovers')[i],
            PF=players_teams.get('PF')[i],
            fgAttempted=players_teams.get('fgAttempted')[i],
            fgMade=players_teams.get('fgMade')[i],
            ftAttempted=players_teams.get('ftAttempted')[i],
            ftMade=players_teams.get('ftMade')[i],
            threeAttempted=players_teams.get('threeAttempted')[i],
            threeMade=players_teams.get('threeMade')[i],
            dq=players_teams.get('dq')[i],
            PostGP=players_teams.get('PostGP')[i],
            PostGS=players_teams.get('PostGS')[i],
            PostMinutes=players_teams.get('PostMinutes')[i],
            PostPoints=players_teams.get('PostPoints')[i],
            PostoRebounds=players_teams.get('PostoRebounds')[i],
            PostdRebounds=players_teams.get('PostdRebounds')[i]
        ))

    f.close()
    
def populate_players(file_path):

    columns = ["bioID", "pos", "firstseason", "lastseason",
              "height", "weight", "birthDate", "college",
              "collegeOther", "birthDate", "deathDate"  
              ]

    players = pd.read_csv('../data/players.csv', usecols=columns)

    f = open(file_path, "a")

    for i in range(len(players.get('bioID'))):
        f.write("INSERT INTO players(bioID, pos, firstseason, lastseason, height, weight, college, collegeOther, birthDate, deathDate) VALUES('{bioID}','{pos}','{firstseason}','{lastseason}','{height}','{weight}','{college}','{collegeOther}','{birthDate}','{deathDate}');\n".format(
            bioID=players.get('bioID')[i],
            pos=players.get('pos')[i],
            firstseason=players.get('firstseason')[i],
            lastseason=players.get('lastseason')[i],
            height=players.get('height')[i],
            weight=players.get('weight')[i],
            college=players.get('college')[i],
            collegeOther=players.get('collegeOther')[i],
            birthDate=players.get('birthDate')[i],
            deathDate=players.get('deathDate')[i]
        ))
    f.close()


def populate_awards_players(file_path):

    columns = ["playerID", "award", "year", "lgID"]

    awards_players = pd.read_csv('../data/awards_players.csv', usecols=columns)

    f = open(file_path, "a")

    for i in range(len(awards_players.get('playerID'))):
        f.write("INSERT INTO awards_players(playerID, award, year, lgID) VALUES('{playerID}','{award}','{year}','{lgID}');\n".format(
            playerID=awards_players.get('playerID')[i],
            award=awards_players.get('award')[i],
            year=awards_players.get('year')[i],
            lgID=awards_players.get('lgID')[i]
        ))

    f.close()


populate_teams_post(path)
populate_coaches(path)
populate_teams(path)
populate_series_post(path)
populate_players_teams(path)
populate_players(path)
populate_awards_players(path)