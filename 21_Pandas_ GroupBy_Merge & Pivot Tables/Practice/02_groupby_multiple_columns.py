
import pandas as pd

data = {
    "Department": ["IT", "HR", "IT", "HR", "IT", "HR"],
    "Region": ["West", "East", "West", "West", "East", "East"],
    "Sales": [5000, 3000, 7000, 4000, 6000, 2000]
}

df = pd.DataFrame(data)

result = df.groupby(
    ["Department", "Region"]
)["Sales"].sum()

print(result)
