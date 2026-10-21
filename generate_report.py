import matplotlib.pyplot as plt

def generate_report():
    # Create report
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.axis("off")

    ax.text(
        0.5, 0.93,
        "SALES DATA CLEANING REPORT",
        fontsize=20,
        fontweight="bold",
        ha="center"
    )

    report = """
PROJECT OVERVIEW
Sales Data Cleaning and Analysis

OBJECTIVES
- Identify missing values
- Remove duplicate records
- Standardize inconsistent data
- Prepare data for analysis

TOOLS USED
- Python
- Pandas
- GitHub

CLEANING PROCESS
1. Load the sales dataset.
2. Inspect data quality.
3. Handle missing values.
4. Remove duplicate records.
5. Save the cleaned dataset.

OUTPUT
Cleaned data prepared for further
analysis and visualization.

CONCLUSION
This project demonstrates how Python
can improve sales data quality and
prepare data for further analysis.
"""

    ax.text(
        0.08, 0.82,
        report,
        fontsize=12,
        va="top",
        linespacing=1.5
    )

    plt.savefig(
        "report.png",
        dpi=150,
        bbox_inches="tight"
    )

    plt.close()
    print("Report generated successfully: report.png")


if __name__ == "__main__":
    generate_report()