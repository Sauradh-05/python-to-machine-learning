
import pandas as pd

data = {
    "Department": ["IT", "HR", "IT", "HR", "IT", "HR"],
    "Sales": [5000, 3000, 7000, 4000, 6000, 2000]
}

df = pd.DataFrame(data)

result = df.groupby("Department")["Sales"].agg(
    ["sum", "mean", "min", "max", "count"]
)

print(result)
