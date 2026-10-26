import pandas as pd

data = {
    "Student Name": ["Yash", "Pratik", "Rohan"],
    "Student Age": [25, 27, 30],
    "Student City": ["Pune", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)

df = df.rename(columns={
    "Student Name": "name",
    "Student Age": "age",
    "Student City": "city"
})

print(df)
print("\nColumn names:")
print(df.columns.tolist())