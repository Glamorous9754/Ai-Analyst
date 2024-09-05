from analysis_engine import ensure_report_directory
import os

def generate_report(desc_stats, charts):
    """Generates a report file including descriptive statistics and chart details."""
    ensure_report_directory()

    with open("Report/analysis_report.txt", "w") as f:
        f.write("Analysis Report\n")
        f.write("====================\n\n")

        f.write("Descriptive Statistics:\n")
        for col in desc_stats.columns:
            f.write(f"{col}:\n")
            for stat in desc_stats.index:
                f.write(f"  {stat}: {desc_stats.at[stat, col]:.2f}\n")
            f.write("\n")

        f.write("Charts Generated:\n")
        for chart in charts:
            chart_name = os.path.basename(chart).replace('.png', '')
            f.write(f"Chart '{chart_name}' has been generated and saved.\n")

    print("Report and charts have been generated successfully.")
