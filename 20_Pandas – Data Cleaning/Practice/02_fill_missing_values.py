import pandas as pd

data = {
    "Name": ["Yash", "Pratik", "Rohan", "Suyash"],
    "Age": [25, None, 30, None],
    "City": ["Pune", None, "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["City"] = df["City"].fillna("Unknown")

print(df)