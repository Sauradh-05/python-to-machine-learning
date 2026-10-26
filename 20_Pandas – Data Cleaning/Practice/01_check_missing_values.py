import pandas as pd

data = {
    "Name": ["Yash", "Pratik", None, "Suyash"],
    "Age": [25, None, 30, 28],
    "City": ["Pune", "Mumbai", None, "Delhi"]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nMissing values:")
print(df.isnull())

print("\nMissing values per column:")
print(df.isnull().sum())