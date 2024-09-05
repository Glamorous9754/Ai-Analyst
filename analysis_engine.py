import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, r2_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt
import os

def ensure_report_directory():
    """Creates a 'Report' directory if it doesn't exist to store charts and reports."""
    if not os.path.exists('Report'):
        os.makedirs('Report')

def create_histograms(df):
    """Generates histograms for numeric columns and saves them as PNG files."""
    histograms = []
    if not df.empty:
        for col in df.columns:
            plt.figure(figsize=(10, 6))
            sns.histplot(df[col], kde=True)
            plt.title(f'Histogram of {col}')
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.tight_layout()
            file_name = f'Report/{col}_histogram.png'
            plt.savefig(file_name)
            plt.close()
            histograms.append(file_name)
    return histograms

def create_top_n_charts(df, top_n):
    """Generates scatter plots for the top N most correlated pairs."""
    corr = df.corr()
    correlations = corr.unstack().sort_values(ascending=False)
    correlations = correlations[correlations != 1]
    top_correlations = correlations.head(top_n)

    charts = []
    for i, (var1, var2) in enumerate(top_correlations.index):
        corr_value = top_correlations[(var1, var2)]
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x=var1, y=var2)
        plt.title(f'Scatter Plot of {var1} vs {var2} (Correlation: {corr_value:.2f})')
        plt.xlabel(var1)
        plt.ylabel(var2)
        plt.tight_layout()
        file_name = f'Report/{var1}_vs_{var2}_scatter.png'
        plt.savefig(file_name)
        plt.close()
        charts.append(file_name)

    return charts

def create_bar_charts(df, top_n):
    """Creates bar charts for categorical columns vs numerical columns."""
    bar_charts = []
    categorical_cols = df.select_dtypes(include=['object']).columns
    numerical_cols = df.select_dtypes(include=['number']).columns

    for cat_col in categorical_cols:
        top_entries = df[cat_col].value_counts().nlargest(top_n).index
        filtered_df = df[df[cat_col].isin(top_entries)]

        for num_col in numerical_cols:
            plt.figure(figsize=(12, 8))
            sns.barplot(x=cat_col, y=num_col, data=filtered_df)
            plt.title(f'{num_col} vs {cat_col} (Top {top_n} Categories)')
            plt.xlabel(cat_col)
            plt.ylabel(num_col)
            plt.tight_layout()
            file_name = f'Report/{cat_col}_vs_{num_col}_bar_chart.png'
            plt.savefig(file_name)
            plt.close()
            bar_charts.append(file_name)

    return bar_charts

def create_line_charts(df):
    """Generates line charts for numeric columns if the index contains datetime values."""
    line_charts = []
    if df.index.to_series().apply(pd.api.types.is_datetime64_any_dtype).any():
        df = df.set_index(df.index.to_series().apply(pd.to_datetime))
        for col in df.columns:
            plt.figure(figsize=(10, 6))
            plt.plot(df.index, df[col])
            plt.title(f'Line Chart of {col} over Time')
            plt.xlabel('Date')
            plt.ylabel(col)
            plt.tight_layout()
            file_name = f'Report/{col}_line_chart.png'
            plt.savefig(file_name)
            plt.close()
            line_charts.append(file_name)
    return line_charts

def normal_analysis(df, top_n):
    """Performs normal analysis by generating histograms, scatter plots, and other charts."""
    ensure_report_directory()

    numeric_df = df.select_dtypes(include=['number'])

    charts = []
    charts.extend(create_histograms(numeric_df))
    charts.extend(create_top_n_charts(numeric_df, top_n))
    charts.extend(create_bar_charts(df, top_n))
    charts.extend(create_line_charts(df))

    desc_stats = numeric_df.describe()

    return desc_stats, charts

def predictive_analysis(df, target_column, model_type):
    """Performs predictive analysis based on classification or regression models."""
    X = df.drop(columns=[target_column])
    y = df[target_column]

    X = pd.get_dummies(X, drop_first=True)

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    models = {}
    if model_type == 'classification':
        models['Linear Discriminant Analysis'] = LDA()
        models['Random Forest Classifier'] = RandomForestClassifier()
    else:
        models['Linear Regression'] = LinearRegression()
        models['Random Forest Regressor'] = RandomForestRegressor()

    model_results = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred_train = model.predict(X_train)
        y_pred_test = model.predict(X_test)

        if model_type == 'classification':
            train_score = accuracy_score(y_train, y_pred_train)
            test_score = accuracy_score(y_test, y_pred_test)
        else:
            train_score = r2_score(y_train, y_pred_train)
            test_score = r2_score(y_test, y_pred_test)

        model_results[name] = (train_score, test_score)

    return model_results, charts
