from user_interface import (
    get_file_path,
    get_clean_option,
    get_analysis_mode,
    get_top_n,
    get_target_column,
    get_model_type
)
from data_processing import load_data, clean_data
from analysis_engine import normal_analysis, predictive_analysis
from report_generation import generate_report

def ask_for_imputation_type():
    # Function to ask for imputation type
    impute_type = input("Enter the imputation type (mean, median, mode): ")
    return impute_type

def ask_for_iqr_multiplier():
    # Function to ask for IQR multiplier
    iqr_multiplier = float(input("Enter the IQR multiplier: "))
    return iqr_multiplier

def main():
    print("Hello! How's it going?")
    print("I'm here to help you analyze your data. Let's get started!")

    # Input dataset file path
    file_path = get_file_path()
    df = load_data(file_path)

    # Input custom data cleaning options
    clean_option = get_clean_option()
    if clean_option == 'yes':
        impute_type = ask_for_imputation_type()  # Assuming ask_for_imputation_type is available
        iqr_multiplier = ask_for_iqr_multiplier()  # Assuming ask_for_iqr_multiplier is available
        df = clean_data(df, mode="custom", impute_type=impute_type, iqr_multiplier=iqr_multiplier)
    else:
        df = clean_data(df)

    # Input analysis mode
    analysis_mode = get_analysis_mode()

    if analysis_mode == '1':
        top_n = get_top_n()
        result, charts = normal_analysis(df, top_n)
        generate_report(result, charts)
    elif analysis_mode == '2':
        target_column = get_target_column()
        model_type = get_model_type()
        model_results, charts = predictive_analysis(df, target_column, model_type)
        generate_report(model_results, charts)
    else:
        print("Invalid choice. Please select 1 for Normal Analysis or 2 for Predictive Analysis.")

if __name__ == "__main__":
    main()
