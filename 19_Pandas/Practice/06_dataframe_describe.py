import pandas as pd

data = {
    "Marks": [85, 90, 78, 92, 81],
    "Age": [24, 23, 25, 22, 26]
}

df = pd.DataFrame(data)

print(df.describe())