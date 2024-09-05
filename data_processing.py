import pandas as pd


def load_data(file_path):
    """Loads the dataset based on the file type (CSV, JSON, Excel)."""
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.json'):
        return pd.read_json(file_path)
    elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file type. Please provide a CSV, JSON, or Excel file.")


def clean_data(df, mode="default", impute_type="mean", iqr_multiplier=0):
    """Cleans the dataset based on missing values and outliers.

    Args:
        df (DataFrame): The dataset to clean.
        mode (str): Default or custom mode for cleaning.
        impute_type (str): Type of imputation to use for missing values (mean, median, mode).
        iqr_multiplier (float): Multiplier for outlier detection using IQR.
    """
    # Handle missing values
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            missing_ratio = df[col].isnull().sum() / len(df[col])
            if missing_ratio < 0.5:
                if mode == "custom":
                    # User-specified imputation method
                    if impute_type == "mean":
                        df[col].fillna(df[col].mean(), inplace=True)
                    elif impute_type == "median":
                        df[col].fillna(df[col].median(), inplace=True)
                    elif impute_type == "mode":
                        df[col].fillna(df[col].mode()[0], inplace=True)
                else:
                    # Default to mean imputation
                    df[col].fillna(df[col].mean(), inplace=True)
            else:
                # Drop column if more than 50% data is missing
                df.drop(col, axis=1, inplace=True)

    # Outlier handling using IQR method
    if iqr_multiplier > 0:
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        Q1 = df[numeric_cols].quantile(0.25)
        Q3 = df[numeric_cols].quantile(0.75)
        IQR = Q3 - Q1

        # Clip outliers based on IQR range
        for col in numeric_cols:
            lower_bound = Q1[col] - iqr_multiplier * IQR[col]
            upper_bound = Q3[col] + iqr_multiplier * IQR[col]
            df[col] = df[col].clip(lower=lower_bound, upper=upper_bound)

    df.to_csv('cleaned.csv', index=False)
    return df
