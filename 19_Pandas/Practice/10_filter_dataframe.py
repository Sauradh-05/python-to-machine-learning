import pandas as pd

data = {
    "Name": ["Yash", "Pratik", "Rahul", "Suyash"],
    "Marks": [85, 90, 65, 92]
}

df = pd.DataFrame(data)

high_scores = df[df["Marks"] >= 85]

print(high_scores)