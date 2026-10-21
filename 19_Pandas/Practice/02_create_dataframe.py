import pandas as pd

data = {
    "Name": ["Yash", "Pratik", "Suyash", "Sauradh"],
    "Age": [24, 23, 25, 26],
    "Marks": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

print(df)