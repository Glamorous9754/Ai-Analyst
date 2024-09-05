---

# AI Employee Prototype for Data Analysis and Reporting

## Project Overview

This AI employee prototype specializes in performing data analysis, generating visual reports, and offering predictive insights based on the provided datasets. The project is designed to handle both normal and predictive analysis through various statistical and machine learning techniques.

## Features

1. **Data Ingestion**:
   - Supports CSV, JSON, and Excel file formats.
   - Automatically loads and processes datasets.

2. **Data Cleaning**:
   - Handles missing values based on custom or default options.
   - Provides outlier detection using the IQR method with a customizable multiplier.

3. **Normal Analysis**:
   - Generates descriptive statistics.
   - Creates histograms, scatter plots, bar charts, and line charts for data visualization.
   - Provides correlation analysis for top N correlated pairs.

4. **Predictive Analysis**:
   - Supports both classification and regression models.
   - Models include Linear Discriminant Analysis (LDA), Random Forest, and Linear Regression.
   - Outputs accuracy or R² scores for train and test data.

5. **Report Generation**:
   - Automatically generates a report file containing:
     - Descriptive statistics
     - List of generated charts and their file paths
   - Outputs charts in PNG format and the report in a TXT file.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/ai-employee-prototype.git
   ```
   
2. **Navigate to the project directory**:
   ```bash
   cd ai-employee-prototype
   ```

3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure necessary libraries are installed**:
   - `pandas`
   - `scikit-learn`
   - `matplotlib`
   - `seaborn`

## Usage

### 1. Data Loading

Run the user interface and follow the prompts to load your dataset:

```bash
python user_interface.py
```

The script will prompt you to provide the path to your dataset (CSV, JSON, or Excel).

### 2. Data Cleaning

Choose whether to apply default or custom data cleaning techniques:
- **Default**: Automatically fills missing values with the mean for numeric columns.
- **Custom**: You can specify how to handle missing values and outliers using various methods (mean, median, mode).

### 3. Normal Analysis

During normal analysis, the system generates:
- Descriptive statistics
- Histograms, scatter plots, bar charts, and line charts
- Reports containing charts and statistical summaries

The analysis results are stored in the `Report/` directory.

### 4. Predictive Analysis

To perform predictive analysis:
- Select a target variable from your dataset.
- Choose between **classification** or **regression** models.

The system will evaluate models and provide accuracy or R² scores for both training and testing data.

### 5. Generating the Report

The report and charts are saved in the `Report/` folder. The report file (`analysis_report.txt`) includes:
- Descriptive statistics
- A list of generated charts with their file paths.

## Project Structure

```plaintext
ai-employee-prototype/
│
├── data_processing.py        # Data ingestion and cleaning functions
├── analysis_engine.py        # Analysis engine for normal and predictive analysis
├── report_generation.py      # Report generation functionality
├── user_interface.py         # Command-line interface for user interaction
├── requirements.txt          # Dependencies for the project
└── Report/                   # Directory for storing generated reports and charts
```

## Example Run

1. Provide the dataset file path when prompted.
2. Choose custom data cleaning if needed.
3. Choose the analysis mode (normal or predictive).
4. View the generated charts and report in the `Report/` directory.

## Requirements

- Python 3.x
- Libraries: `pandas`, `seaborn`, `matplotlib`, `scikit-learn`

Install all dependencies via:

```bash
pip install -r requirements.txt
```

## Author

Ayan Das (GitHub: [Glamorous9754](https://github.com/Glamorous9754))

---
