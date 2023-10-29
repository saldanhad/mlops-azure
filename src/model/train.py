# Import libraries

import argparse
import glob
import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import mlflow

# Define functions

def main(args):
    # TO DO: enable autologging
    mlflow.azureml.autolog()

    # Read data
    df = get_csvs_df(args.training_data)

    # Split data
    X_train, X_test, y_train, y_test = split_data(df)

    # Train model
    train_model(args.reg_rate, X_train, X_test, y_train, y_test)

def get_csvs_df(path):
    
    if not os.path.exists(path):
        raise RuntimeError(f"Cannot use a non-existent path provided: {path}")
    csv_files = glob.glob(f"{path}/*.csv")
    if not csv_files:
        raise RuntimeError(f"No CSV files found in path: {path}")
    return pd.concat((pd.read_csv(f) for f in csv_files), sort=True)  # Set sort=True if column order matters

# TO DO: add a function to split data

def split_data(df):
    X = df[['Pregnancies', 'PlasmaGlucose', 'DiastolicBloodPressure', 'TricepsThickness', 'SerumInsulin', 'BMI', 'DiabetesPedigree', 'Age']].values
    y = df['Diabetic'].values
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
    return X_train, X_test, y_train, y_test

def train_model(reg_rate, X_train, X_test, y_train, y_test):
    # Train model
    LogisticRegression(C=1/reg_rate, solver="liblinear").fit(X_train, y_train)
    

def parse_args():
    # Setup arg parser
    parser = argparse.ArgumentParser()

    # Add arguments
    parser.add_argument("--training_data", dest='training_data', type=str)
    parser.add_argument("--reg_rate", dest='reg_rate', type=float, default=0.01)

    # Parse args
    args = parser.parse_args()

    # Return args
    return args

# Run script
if __name__ == "__main__":
    # Add space in logs
    print("\n\n")
    print("*" * 60)

    # Parse args
    args = parse_args()

    # Run the main function
    main(args)

    # Add space in logs
    print("*" * 60)
    print("\n\n")

