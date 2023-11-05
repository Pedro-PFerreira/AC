import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

def replace_tmID(df):

    unique_values = df["tmID"].unique()
    value_to_index = {value: idx for idx, value in enumerate(unique_values)}

    # Replace values with their respective index
    df["tmID"] = df["tmID"].replace(value_to_index)

def merge():

    # Retrieve the merged the data

    df = pd.read_csv('new_final_dataset.csv', delimiter=';')

    # Replace tmID for an number, in order to be 
    # used in the classification model

    replace_tmID(df)

    # Drop the rows have invalid values

    df = df[~(df["height"] < 30)]
    df = df[~(df["height"] == 0)]
    df = df[~(df["deathDate"] != "0000-00-00")]

    # Drop the columns that are not needed

    df = df.drop(["lgID", "homeL", "playerID",
                 "college", "collegeOther", "birthDate",
                 "deathDate", "firstseason", "lastseason", 
                 "post_losses", "pos"], axis=1)
    
    # Shift the playoff-related data of a year to the next one

    df["playoff"] = df["playoff"].shift(1)
    df["firstRound"] = df["firstRound"].shift(1)
    df["semis"] = df["semis"].shift(1)
    df["finals"] = df["finals"].shift(1)
    df["postPlayerScore"] = df["postPlayerScore"].shift(1)
    df["postThreeAccuracy"] = df["postThreeAccuracy"].shift(1)
    df["post_wins"] = df["post_wins"].shift(1)


    # Split the dataset into train and test

    train = df[(df["year"] < 8) & (df["year"] > 1)]
    test = df[df["year"] >= 8]

    # Split into features and labels

    train_features = train.drop(["playoff"], axis=1)
    
    train_label = train["playoff"]

    test_features = test.drop(["playoff"], axis=1)

    test_label = test["playoff"]

    # Create the model

    model = DecisionTreeClassifier()

    # Train the model

    model.fit(train_features, train_label)

    # Predict the test data

    predictions = model.predict(test_features)

    # Calculate the accuracy

    accuracy = np.mean(predictions == test_label)

    print(accuracy)


merge()