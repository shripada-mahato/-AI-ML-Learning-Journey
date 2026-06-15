import pandas as pd
result = pd.read_csv("archive/ecommerce_dataset_updated.csv")
print_rows = result["Category","Payment_Method","Purchase_Date","Discount (%)"]
print(print_rows.head().to_string())