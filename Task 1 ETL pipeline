# etl_pipeline.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Extract: Load dataset
print("Loading dataset...")
df = pd.read_csv("titanic.csv")

# Transform: Clean and preprocess the data
print("Cleaning and transforming data...")

# Drop irrelevant columns
columns_to_drop = ['PassengerId', 'Name', 'Ticket', 'Cabin']
df.drop(columns=columns_to_drop, inplace=True)

# Fill missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Encode categorical features
label_encoders = {}
categorical_columns = ['Sex', 'Embarked']

for column in categorical_columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Scale numerical features
scaler = StandardScaler()
numerical_columns = ['Age', 'Fare']
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

# Load: Save the cleaned dataset to CSV
df.to_csv("titanic_cleaned.csv", index=False)
print("ETL process completed successfully. Cleaned data saved to 'titanic_cleaned.csv'.")
