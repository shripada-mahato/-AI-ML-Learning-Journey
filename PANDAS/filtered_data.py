import pandas as pd
data = pd.read_csv("archive/ecommerce_dataset_updated.csv")
#separate first 50 data from 3660 data for practicing
result = data.head(51)

#separate "Sports" from category column
category = result[result["Category"]=="Sports"].to_string(index=True)
print("category sport\n")
print(category)

#price > 250 from the "price(Rs.)"
print("price > 250\n")
price = result[result["Price (Rs.)"]>250]
print(price.to_string())
