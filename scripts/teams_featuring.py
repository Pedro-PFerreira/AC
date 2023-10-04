import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import sklearn.tree as tree
from sklearn.model_selection import cross_val_score

def createCorrelationMatrix():

    # Load the dataset

    df = pd.read_csv('data/cleaned/teams_merged.csv')

    # # See the correlation matrix between the features

    # corr = df.corr()

    # # Plot the correlation matrix between the features

    # plt.figure(figsize=(10, 8))  # Set the figure size
    # sb.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    # plt.show()

    # Drop the columns that are highly correlated to each other

    df = df.drop(['o_fga','o_3pm','o_3pa','o_dreb','o_reb'], axis=1)

    df = df.drop(['d_pts', 'd_fgm', 'd_dreb', 
                'd_fta', 'd_ftm', 'd_oreb',
                'd_stl', 'd_asts', 'd_blk',
                'd_pf', 'd_to', 'd_3pa',
                'd_reb', 'd_fga', 'd_3pm'], axis=1)

    df = df.drop('GP', axis=1)

    # Plot the correlation matrix between the features

    new_corr = df.corr()
    plt.figure(figsize=(10, 8))  # Set the figure size
    sb.heatmap(new_corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.show()


def featureSelection():

    # Load the dataset

    df = pd.read_csv('data/cleaned/teams_merged.csv')

    # Drop the columns that are highly correlated to each other

    df = df.drop(['o_fga','o_3pm','o_3pa','o_dreb','o_reb'], axis=1)

    df = df.drop(['d_pts', 'd_fgm', 'd_dreb', 
                'd_fta', 'd_ftm', 'd_oreb',
                'd_stl', 'd_asts', 'd_blk',
                'd_pf', 'd_to', 'd_3pa',
                'd_reb', 'd_fga', 'd_3pm'], axis=1)

    df = df.drop('GP', axis=1)

    # For a specific model, determine the accuracy with the selected variables

    decision_tree = tree.DecisionTreeClassifier()

    # Split the dataset into training and testing sets

    train = df[df['year'] < 8]

    test = df[df['year'] >= 8]

    # Split the training set into features and labels

    train_features = train.drop('playoff', axis=1)

    train_labels = train['playoff']

    # Split the testing set into features and labels

    test_features = test.drop('playoff', axis=1)

    test_labels = test['playoff']

    # Fit the model to the training set

    decision_tree.fit(train_features, train_labels)

    # Predict the labels of the test set

    predictions = decision_tree.predict(test_features)

    # Calculate the accuracy of the model

    accuracy = (predictions == test_labels).sum() / len(predictions)

    print('Accuracy of the model: ', accuracy)

    # Calculate the cross validation score

    cross_val = cross_val_score(decision_tree, train_features, train_labels, cv=10)

    print('Cross validation score: ', cross_val.mean())

    # Plot the decision tree

    plt.figure(figsize=(20, 20))

    tree.plot_tree(decision_tree, feature_names=train_features.columns, class_names=['No', 'Yes'], filled=True)

    plt.show()


featureSelection()