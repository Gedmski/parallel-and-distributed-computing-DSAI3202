import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import os

print(os.getcwd())

def prepare():
    # Load the train_dataset
    file_path = '/home/student/parallel-and-distributed-computing-DSAI3202/data/train.csv'
    train_data = pd.read_csv(file_path, index_col="Id")
    
    # Columns to be deleted
    columns_to_delete = ['MoSold', 'YrSold', 'SaleType', 'SaleCondition', 'Alley', 'FireplaceQu', 'PoolQC', 'Fence', 'MiscFeature']
    
    # Delete the specified columns
    train_data_cleaned = train_data.drop(columns=columns_to_delete, axis=1)
    
    # Define the input features (X) and the output (y)
    X = train_data_cleaned.drop('SalePrice', axis=1)
    y = train_data_cleaned['SalePrice']
    
    # Identify the categorical columns in X
    categorical_columns = X.select_dtypes(include=['object']).columns
    
    # Initialize a LabelEncoder for each categorical column
    label_encoders = {column: LabelEncoder() for column in categorical_columns}
    
    # Apply Label Encoding to each categorical column
    for column in categorical_columns:
        X[column] = label_encoders[column].fit_transform(X[column])
    
    # Split the first dataset (X, y) into train and test sets with a 70% - 30% split
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.30, random_state=42)
    
    # Fill NaN values in X_train and X_val with the median of the respective columns
    X_train_filled = X_train.fillna(X_train.median())
    X_val_filled = X_val.fillna(X_val.median())

    return X_train_filled, X_val_filled, y_train, y_val