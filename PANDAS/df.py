import pandas as pd

data = {
    "NAME":['RAM','SAM','RAMESH','KRITI'],
    'ROLL':[54,98,3,98],
    'DEPT':['CS','MANAGEMENT','FINANCE','PSYCHOLOGY']
}

df = pd.DataFrame(data)
print(df.to_string())