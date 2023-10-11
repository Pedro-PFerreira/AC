import pandas as pd

# Read the CSV file from players, awards_player and coaches
players = pd.read_csv('../data/players.csv')
awards_players = pd.read_csv('../data/awards_players.csv')
coaches = pd.read_csv('../data/coaches.csv')

# Create a new column in players and coaches
players.insert(2, column = "number_awards", value = 0)
coaches.insert(2, column = "number_awards", value = 0)

df = pd.DataFrame({"id", "year", "tmID"})
df["number_awards"] = 0

# Do the count of awards that a player or a coach won
for (line in awards_players):
    count = 0
    if(coaches['id'].contains(line.get('id'))){
        for (next_line in awards_players):
            if(line.get("id") == next_line.get("id")) count+1

        df.loc[line.get("id"), "number_awards"] = count
        df.to_csv("coaches.csv", index = False)    
    }

    else {
        for (next_line in awards_players):
            if(line.get("id") == next_line.get("id")) count+1

         df.loc[line.get("id"), "number_awards"] = count
         df.to_csv("players.csv", index = False)   
    }

    