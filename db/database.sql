DROP TABLE IF EXISTS teams_post;
DROP TABLE IF EXISTS coaches;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS series_post;
DROP TABLE IF EXISTS players_teams;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS awards_players;

-- teams_post Table
CREATE TABLE teams_post (
    year INT NOT NULL,
    tmID VARCHAR(255) NOT NULL,
    lgID VARCHAR(255) NOT NULL,
    W INT,
    L INT,
    PRIMARY KEY (year, tmID, lgID),
    FOREIGN KEY (tmID, lgID) REFERENCES teams(tmID, lgID)
);

-- coaches Table
CREATE TABLE coaches (
    coachID VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    tmID VARCHAR(255) NOT NULL,
    lgID VARCHAR(255) NOT NULL,
    stint INT NOT NULL,
    won INT,
    lost INT,
    post_wins INT,
    post_losses INT,
    PRIMARY KEY (coachID, year, tmID, lgID, stint),
    FOREIGN KEY (tmID, lgID) REFERENCES teams(tmID, lgID)
);

-- teams Table
CREATE TABLE teams (
    year INT NOT NULL,
    lgID VARCHAR(255) NOT NULL,
    tmID VARCHAR(255) NOT NULL,
    franchID VARCHAR(255),
    confID VARCHAR(255),
    divID VARCHAR(255),
    rank INT,
    playoff VARCHAR(255),
    seeded INT,
    firstRound VARCHAR(255),
    semis VARCHAR(255),
    finals VARCHAR(255),
    name VARCHAR(255) NOT NULL,
    o_fgm INT,
    o_fga INT,
    o_ftm INT,
    o_fta INT,
    o_3pm INT,
    o_3pa INT,
    o_oreb INT,
    o_dreb INT,
    o_reb INT,
    o_asts INT,
    o_pf INT,
    o_stl INT,
    o_to INT,
    o_blk INT,
    o_pts INT,
    d_fgm INT,
    d_fga INT,
    PRIMARY KEY (year, lgID, tmID),
    FOREIGN KEY (lgID) REFERENCES leagues(lgID),
    FOREIGN KEY (franchID) REFERENCES franchises(franchID),
    FOREIGN KEY (confID) REFERENCES conferences(confID),
    FOREIGN KEY (divID) REFERENCES divisions(divID)
);

-- series_post Table
CREATE TABLE series_post (
    year INT NOT NULL,
    round VARCHAR(255) NOT NULL,
    series VARCHAR(255) NOT NULL,
    tmIDWinner VARCHAR(255) NOT NULL,
    lgIDWinner VARCHAR(255) NOT NULL,
    tmIDLoser VARCHAR(255) NOT NULL,
    lgIDLoser VARCHAR(255) NOT NULL,
    W INT NOT NULL,
    L INT NOT NULL,
    PRIMARY KEY (year, round, series),
    FOREIGN KEY (tmIDWinner, lgIDWinner) REFERENCES teams(tmID, lgID),
    FOREIGN KEY (tmIDLoser, lgIDLoser) REFERENCES teams(tmID, lgID)
);

-- players_teams Table
CREATE TABLE players_teams (
    playerID VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    stint INT NOT NULL,
    tmID VARCHAR(255) NOT NULL,
    lgID VARCHAR(255) NOT NULL,
    GP INT,
    GS INT,
    minutes INT,
    points INT,
    oRebounds INT,
    dRebounds INT,
    rebounds INT,
    assists INT,
    steals INT,
    blocks INT,
    turnovers INT,
    PF INT,
    fgAttempted INT,
    fgMade INT,
    ftAttempted INT,
    ftMade INT,
    threeAttempted INT,
    threeMade INT,
    dq INT,
    PostGP INT,
    PostGS INT,
    PostMinutes INT,
    PostPoints INT,
    PostoRebounds INT,
    PostdRebounds INT,
    PRIMARY KEY (playerID, year, stint, tmID, lgID),
    FOREIGN KEY (playerID) REFERENCES players(playerID),
    FOREIGN KEY (tmID, lgID) REFERENCES teams(tmID, lgID)
);

-- players Table
CREATE TABLE players (
    bioID VARCHAR(255) NOT NULL PRIMARY KEY,
    pos VARCHAR(255),
    firstseason INT,
    lastseason INT,
    height FLOAT,
    weight INT,
    college VARCHAR(255),
    collegeOther VARCHAR(255),
    birthDate VARCHAR(255),
    deathDate VARCHAR(255)
);

-- awards_players Table
CREATE TABLE awards_players (
    playerID VARCHAR(255) NOT NULL,
    award VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    lgID VARCHAR(255) NOT NULL,
    PRIMARY KEY (playerID, award, year, lgID),
    FOREIGN KEY (playerID) REFERENCES players(playerID)
);