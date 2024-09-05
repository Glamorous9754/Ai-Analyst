import pandas as pd

def get_file_path():
    return input("Provide the dataset file path:\n")

def get_clean_option():
    return input("Use custom data cleaning options?\n")

def get_analysis_mode():
    return input(
        "Select analysis mode:\n1. Normal Analysis\n2. Predictive Analysis\nEnter the number corresponding to your choice: "
    )

def get_top_n():
    return int(input("Enter the number of top correlations to display:\n"))

def get_target_column():
    return input("Enter the target column for predictive analysis:\n")

def get_model_type():
    return input("Enter the model type (classification/regression):\n")
