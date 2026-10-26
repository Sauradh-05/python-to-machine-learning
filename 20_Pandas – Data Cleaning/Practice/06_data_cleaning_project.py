import pandas as pd

data = {
    "Student Name": [
        "Yash", "Pratik", "Rohan", "Pratik", None
    ],
    "Student Age": [25, None, 30, None, 22],
    "Student City": [
        "Pune", "Mumbai", "Delhi", "Mumbai", None
    ],
    "Marks": [85, 90, 78, 90, None]
}

df = pd.DataFrame(data)

print("Original dataset:")
print(df)

# Rename columns
df = df.rename(columns={
    "Student Name": "name",
    "Student Age": "age",
    "Student City": "city"
})

# Remove rows with missing names
df = df.dropna(subset=["name"])

# Fill missing numeric values with column medians
for column in ["age", "Marks"]:
    df[column] = df[column].fillna(df[column].median())

# Fill missing city values
df["city"] = df["city"].fillna("Unknown")

# Remove duplicate records
df = df.drop_duplicates()

print("\nCleaned dataset:")
print(df)

print("\nRemaining missing values:")
print(df.isnull().sum())

# Save the cleaned dataset
df.to_csv("cleaned_students.csv", index=False)