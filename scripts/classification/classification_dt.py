import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('new_final_dataset.csv', delimiter=';')

def replace_values(df, column):
    unique_values = df[column].unique()
    value_to_index = {value: idx for idx, value in enumerate(unique_values)}
    df[column] = df[column].replace(value_to_index)

# replace tmID for a number, in order to be used in the classification model
replace_values(df, 'tmID')

# replace bioID for a number, in order to be used in the classification model
replace_values(df, 'bioID')

# drop the columns that are not needed
df = df.drop(['rank', 'pos', 'dq', 'PostDQ'], axis=1)

# replace missing values with the mean
df = df.fillna(df.mean())

# Create a list to store the accuracy for each year
accuracies = []

# Define the sliding window size (e.g., 1 year)
window_size = 1

for year in range(2, 10):
    # Select the data for the current year
    current_year_data = df[df['year'] == year]
    
    # Select the data for the previous years as training data
    training_data = df[df['year'].isin(range(year - window_size, year))]
    
    # Split the training and test datasets
    train_features = training_data.drop(['playoff'], axis=1)
    train_label = training_data['playoff']
    test_features = current_year_data.drop(['playoff'], axis=1)
    test_label = current_year_data['playoff']
    
    # Create the model
    model = DecisionTreeClassifier()
    
    # Train the model
    model.fit(train_features, train_label)
    
    # Predict the test data
    predictions = model.predict(test_features)
    
    # Calculate the accuracy for the current year
    accuracy = np.mean(predictions == test_label)
    accuracies.append(accuracy)
    
    print(f"The accuracy for year {year} is: {accuracy}")

    # Calculate the precision for the current year

    precision = np.mean(predictions[predictions == 1] == test_label[predictions == 1])
    print(f"The precision for year {year} is: {precision}")

    # Calculate the F-measure for the current year

    f_measure = 2 * (precision * accuracy) / (precision + accuracy)

    print(f"The F-measure for year {year} is: {f_measure}")


# Calculate the overall accuracy across all years
overall_accuracy = np.mean(accuracies)
print(f"The overall accuracy of the model is: {overall_accuracy}")

# Calculate the overall precision across all years
overall_precision = np.mean(precision)
print(f"The overall precision of the model is: {overall_precision}")

# Calculate the overall F-measure across all years
overall_f_measure = 2 * (overall_precision * overall_accuracy) / (overall_precision + overall_accuracy)
print(f"The overall F-measure of the model is: {overall_f_measure}")
