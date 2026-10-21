import pandas as pd

data = {
    "Name": ["Yash", "Pratik", "Rahul"],
    "Age": [24, 23, 25],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df["Name"])
print(df[["Name", "Marks"]])