import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "Telco_Customer_Churn_Dataset  (3).csv"

df = pd.read_csv(file_path)

print("Dataset shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

output_dir = "telco_visualization_output"
os.makedirs(output_dir, exist_ok=True)


shortest_tenure = df.sort_values("tenure")
longest_tenure = df.sort_values("tenure", ascending=False)

print("\nCustomers with shortest tenure:")
print(
    shortest_tenure[
        ["customerID", "gender", "tenure", "MonthlyCharges", "Churn"]
    ].head(10)
)

print("\nCustomers with longest tenure:")
print(
    longest_tenure[
        ["customerID", "gender", "tenure", "MonthlyCharges", "Churn"]
    ].head(10)
)

churned = df[df["Churn"] == "Yes"]

print("\nNumber of churned customers:", len(churned))
print("\nChurned customers:")
print(churned.head(10))

with pd.ExcelWriter(
    os.path.join(output_dir, "Task_1_Data_Overview.xlsx"),
    engine="openpyxl"
) as writer:
    df.head(20).to_excel(writer, sheet_name="Dataset_Sample", index=False)
    shortest_tenure.to_excel(writer, sheet_name="Shortest_Tenure", index=False)
    longest_tenure.to_excel(writer, sheet_name="Longest_Tenure", index=False)
    churned.to_excel(writer, sheet_name="Churned_Customers", index=False)


churn_counts = df["Churn"].value_counts().reindex(["No", "Yes"])

print("\nChurn counts:")
print(churn_counts)

plt.figure(figsize=(8, 5))

bars = plt.bar(
    ["Non-Churned", "Churned"],
    churn_counts.values
)

plt.title("Customer Churn Count")
plt.xlabel("Churn Status")
plt.ylabel("Number of Customers")

for bar in bars:
    value = int(bar.get_height())
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value,
        str(value),
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig(
    os.path.join(output_dir, "Task_2_Churn_Count.png"),
    dpi=300,
    bbox_inches="tight"
)
plt.show()
plt.close()


print("\nMonthly Charges:")
print(df["MonthlyCharges"].describe())

min_charge = int(df["MonthlyCharges"].min() // 10 * 10)
max_charge = int((df["MonthlyCharges"].max() // 10 + 1) * 10)

bins = range(min_charge, max_charge + 10, 10)

plt.figure(figsize=(9, 5))

plt.hist(
    df["MonthlyCharges"],
    bins=bins,
    edgecolor="black"
)

plt.title("Distribution of Monthly Charges")
plt.xlabel("Monthly Charges")
plt.ylabel("Number of Customers")
plt.xticks(range(min_charge, max_charge + 10, 10))

plt.tight_layout()
plt.savefig(
    os.path.join(output_dir, "Task_3_MonthlyCharges_Histogram.png"),
    dpi=300,
    bbox_inches="tight"
)
plt.show()
plt.close()


gender_churn = pd.crosstab(
    df["gender"],
    df["Churn"]
).reindex(columns=["No", "Yes"], fill_value=0)

gender_churn = gender_churn.rename(
    columns={
        "No": "Non-Churned",
        "Yes": "Churned"
    }
)

print("\nChurn by gender:")
print(gender_churn)

gender_churn.to_excel(
    os.path.join(output_dir, "Task_4_Gender_Churn_Pivot.xlsx")
)

ax = gender_churn.plot(
    kind="bar",
    figsize=(9, 5)
)

plt.title("Churn Counts by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.legend(title="Churn Status")

for container in ax.containers:
    ax.bar_label(container, fmt="%d", padding=3)

plt.tight_layout()
plt.savefig(
    os.path.join(output_dir, "Task_4_Churn_by_Gender.png"),
    dpi=300,
    bbox_inches="tight"
)
plt.show()
plt.close()

gender_churn_rate = (
    pd.crosstab(
        df["gender"],
        df["Churn"],
        normalize="index"
    )["Yes"] * 100
).round(2)

print("\nChurn rate by gender:")
print(gender_churn_rate)


tenure_bins = [-1, 12, 24, 36, 48, 60, 72]
tenure_labels = [
    "0-12",
    "13-24",
    "25-36",
    "37-48",
    "49-60",
    "61-72"
]

df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=tenure_bins,
    labels=tenure_labels
)

charge_min = int(df["MonthlyCharges"].min() // 10 * 10)
charge_max = int((df["MonthlyCharges"].max() // 10 + 1) * 10)

charge_bins = list(range(charge_min, charge_max + 10, 10))

df["MonthlyChargeGroup"] = pd.cut(
    df["MonthlyCharges"],
    bins=charge_bins,
    right=False
)

df["ChurnNumeric"] = df["Churn"].map({
    "No": 0,
    "Yes": 1
})

heatmap_data = pd.pivot_table(
    df,
    values="ChurnNumeric",
    index="TenureGroup",
    columns="MonthlyChargeGroup",
    aggfunc="mean",
    observed=False
) * 100

print("\nHeatmap data:")
print(heatmap_data.round(2))

heatmap_data.round(2).to_excel(
    os.path.join(output_dir, "Task_5_Heatmap_Data.xlsx")
)

plt.figure(figsize=(14, 6))

sns.heatmap(
    heatmap_data,
    annot=True,
    fmt=".1f",
    cmap="YlOrRd",
    linewidths=0.5,
    cbar_kws={"label": "Churn Rate (%)"}
)

plt.title("Churn Rate by Tenure and Monthly Charges")
plt.xlabel("Monthly Charges Range")
plt.ylabel("Tenure Range (Months)")

plt.tight_layout()
plt.savefig(
    os.path.join(output_dir, "Task_5_Tenure_MonthlyCharges_Heatmap.png"),
    dpi=300,
    bbox_inches="tight"
)
plt.show()
plt.close()

print("\nAll tasks are completed.")
print("Files are saved in:", os.path.abspath(output_dir))
