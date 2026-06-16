import pandas as pd

data = {
    "NAME":['RAM','SAM','RAMESH','KRITI'],
    'ROLL':[54,98,3,98],
    'DEPT':['CS','MANAGEMENT','FINANCE','PSYCHOLOGY']
}
df = pd.DataFrame(data)
add_new_column = df.insert(3,"Marks",[98,67,97,25])

filter_data = df[df["Marks"]>80]
print(filter_data.to_string(index=False))