
import pandas as pd

data = {
    "Employee": ["Yash", "Pratik", "Yash", "Rahul", "Pratik"],
    "Sales": [1000, 2000, 1500, 3000, 2500]
}

df = pd.DataFrame(data)

# Calculate total sales by employee
result = df.groupby("Employee")["Sales"].sum()

print(result)
