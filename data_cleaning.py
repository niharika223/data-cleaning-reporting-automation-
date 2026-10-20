import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the original dataset
df = pd.read_csv("sales_data.csv")

print("DATA CLEANING AND REPORTING AUTOMATION")
print("=" * 40)

# 2. Display original dataset
print("\nOriginal Dataset:")
print(df.head())

# 3. Check missing values
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# 4. Remove duplicate records
duplicates = df.duplicated().sum()
print("\nDuplicate Records Found:", duplicates)
df = df.drop_duplicates()

# 5. Handle missing values
for column in df.columns:
    if df[column].dtype == "object":
        df[column] = df[column].fillna("Unknown")
    else:
        median_value = df[column].median()
        df[column] = df[column].fillna(median_value)

# 6. Remove unnecessary spaces from text
for column in df.select_dtypes(include=["object"]).columns:
    df[column] = df[column].str.strip()

# 7. Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# 8. Generate sales report
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Sales"] = df["Sales"].fillna(0)

summary = df.groupby("Product")["Sales"].sum()

plt.figure(figsize=(10, 6))
summary.plot(kind="bar")
plt.title("Sales Report by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("report.png")
plt.close()

# 9. Display sales summary
print("\nSALES SUMMARY")
print("-" * 30)
print("Total Records:", len(df))
print("Total Sales:", df["Sales"].sum())
print("Average Sales:", round(df["Sales"].mean(), 2))
print("Highest Sale:", df["Sales"].max())
print("Lowest Sale:", df["Sales"].min())

print("\nCleaned dataset saved as cleaned_data.csv")
print("Sales visualization saved as report.png")
print("Data cleaning and reporting completed successfully!")