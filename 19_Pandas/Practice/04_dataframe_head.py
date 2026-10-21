import pandas as pd

data = {
    "Name": ["Yash", "Pratik", "Suyash", "Sauradh", "KP"],
    "Marks": [85, 90, 78, 92, 81]
}

df = pd.DataFrame(data)

print(df.head())
print(df.head(3))