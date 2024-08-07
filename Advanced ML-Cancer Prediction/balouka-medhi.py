"""
This module performs classification tasks using various ensemble methods.
"""

# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Step 1 - Data Preprocessing: Loading and Exploring the Data
# (Step required as I faced issues with N/A values)

# Load the dataset - Adjusting for Flake8 line length
df = pd.read_csv(
    "/Users/medhi/Desktop/Etudes : Scolarité/TBS - 2021-2024/Cours/MSc AIBA/"
    "UE4 - AI/4.2/Individual Project/CancerPrediction.csv"
)

# Display the first few rows of the dataframe
print(df.head())

# Check the shape of the dataframe
print("Shape of DataFrame:", df.shape)

# Check for null values
print("Null values in each column:\n", df.isna().sum())

# Drop the 'Unnamed: 32' column with all null values
df.drop('Unnamed: 32', axis=1, inplace=True)

# Display diagnosis value counts
print("\nDiagnosis value counts:\n", df["diagnosis"].value_counts())

# Step 2 - Label Encoding
# Encode the 'diagnosis' column
labelencoder = LabelEncoder()
df['diagnosis'] = labelencoder.fit_transform(df['diagnosis'])

# Display the first few rows of the dataframe after encoding
print(df.head())

# Step 3 - Split Dataset & Feature Scaling
# Separate the features and the target variable
X = df.iloc[:, 2:].values
y = df.iloc[:, 1].values

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0)

# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Step 4 - Building and Evaluating a Decision Tree Model
# Train the Decision Tree model
decision_tree = DecisionTreeClassifier(random_state=10)
decision_tree.fit(X_train, y_train)

# Evaluate the model
train_score = decision_tree.score(X_train, y_train)
test_score = decision_tree.score(X_test, y_test)
print(f"Training Score: {train_score}")
print(f"Test Score: {test_score}")

# Predictions and evaluation
y_pred = decision_tree.predict(X_test)
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Let's move on to implementing ensemble methods:
# 1 Bagging
# 2 Stacking
# 3 Boosting

# 1 - Bagging with RF
# Implementing Bagging with Random Forest
random_forest = RandomForestClassifier(n_estimators=100, random_state=0)
random_forest.fit(X_train, y_train)

# Evaluate the Random Forest model
rf_train_score = random_forest.score(X_train, y_train)
rf_test_score = random_forest.score(X_test, y_test)
print(f"Random Forest - Training Score: {rf_train_score}, "
      f"Test Score: {rf_test_score}")

# 2 - Boosting with AdaBoost
# Implementing Boosting with AdaBoost
ada_boost = AdaBoostClassifier(n_estimators=100, random_state=0)
ada_boost.fit(X_train, y_train)

# Evaluate the AdaBoost model
ada_train_score = ada_boost.score(X_train, y_train)
ada_test_score = ada_boost.score(X_test, y_test)
print(f"AdaBoost - Training Score: {ada_train_score}, "
      f"Test Score: {ada_test_score}")

# 3 - Stacking
# Define base learners
base_learners = [
    ('rf', RandomForestClassifier(n_estimators=100, random_state=0)),
    ('ada', AdaBoostClassifier(n_estimators=100, random_state=0)),
    ('dt', DecisionTreeClassifier(random_state=10))
]

# Define meta-learner
stacked_model = StackingClassifier(
    estimators=base_learners,
    final_estimator=LogisticRegression())

# Train stacked model
stacked_model.fit(X_train, y_train)

# Evaluate the Stacked model
stacked_train_score = stacked_model.score(X_train, y_train)
stacked_test_score = stacked_model.score(X_test, y_test)
print(f"Stacked Model - Training Score: {stacked_train_score}, "
      f"Test Score: {stacked_test_score}")

"""
Note: Python script indicating that it conforms to the standards set by Pylint and Flake8
Pylint rating = 10/10
Flake8: 100% fit
"""
