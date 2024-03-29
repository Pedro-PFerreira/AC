import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('final_dataset.csv', delimiter=';')

# split the dataset into train and test

train = df[((df['year'] < 8) & (df['year'] > 1))]

test = df[df['year'] >= 7]

# split into features and labels

train_features = train.drop(['playoff'], axis=1)

train_label = train['playoff']

test_features = test.drop(['playoff'], axis=1)

test_label = test['playoff']

# create the model

model = DecisionTreeClassifier()

# train the model

model.fit(train_features, train_label)

# predict the test data

predictions = model.predict(test_features)

# calculate the accuracy

accuracy = np.mean(predictions == test_label)

print(f"The accuracy of the model is: {accuracy}.")

# calculate the precision

precision = np.mean(predictions[predictions == 1] == test_label[predictions == 1])

print(f"The precision of the model is: {precision}.")

# calculate the f-measure

recall = np.mean(predictions[predictions == 1] == test_label[predictions == 1])

f_measure = 2 * (precision * recall) / (precision + recall)

print(f"The f-measure of the model is: {f_measure}.")