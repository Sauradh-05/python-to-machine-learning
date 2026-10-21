import pandas as pd

data = [
    ["Yash", 85],
    ["Pratik", 90],
    ["Suyash", 78]
]

df = pd.DataFrame(data, columns=["Name", "Marks"])

print(df)