import pandas as pd

data = {
    "Name": ["Yash", "Pratik", "Yash", "Rohan", "Pratik"],
    "Age": [25, 27, 25, 30, 27],
    "City": ["Pune", "Mumbai", "Pune", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)

print("Original dataset:")
print(df)

print("\nDuplicate records:")
print(df[df.duplicated()])

cleaned_df = df.drop_duplicates()

print("\nAfter removing duplicates:")
print(cleaned_df)