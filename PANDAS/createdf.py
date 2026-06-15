import pandas as pd

df = {
    "name":["rahul","sameer","manik","mukull"],
    "roll":[55,98,23,45],
    "percentile":[98,83,79,95],
    "dept":["btech","mba","bpharm","mphil"],
    "city":["kolkata","noida","delhi","gurugaon"]
}

data = pd.DataFrame(df)
print(data)

highest = data[data["percentile"]>90]
print(highest)