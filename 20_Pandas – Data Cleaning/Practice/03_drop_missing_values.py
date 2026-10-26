import pandas as pd

data = {
    "Name": ["Yash", "Pratik", None, "Rohan"],
    "Age": [25, 27, 30, None],
    "City": ["Pune", "Mumbai", "Delhi", "Pune"]
}

df = pd.DataFrame(data)

print("Original dataset:")
print(df)

cleaned_df = df.dropna()

print("\nDataset after removing rows with missing values:")
print(cleaned_df)