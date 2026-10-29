
import pandas as pd

data = {
    "Employee": ["Yash", "Yash", "Pratik", "Pratik", "Rahul", "Rahul"],
    "Region": ["West", "East", "West", "East", "West", "East"],
    "Sales": [5000, 3000, 4000, 6000, 7000, 2000]
}

df = pd.DataFrame(data)

result = pd.pivot_table(
    df,
    values="Sales",
    index="Employee",
    columns="Region",
    aggfunc="sum",
    fill_value=0
)

print(result)
