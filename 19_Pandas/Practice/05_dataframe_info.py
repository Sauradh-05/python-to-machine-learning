import pandas as pd

data = {
    "Name": ["Yash", "Pratik", "Suyash"],
    "Age": [24, 23, 25],
    "Marks": [85.5, 90.0, 78.5]
}

df = pd.DataFrame(data)

df.info()