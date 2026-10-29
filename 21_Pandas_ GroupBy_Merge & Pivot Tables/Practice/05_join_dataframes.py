
import pandas as pd

employees = pd.DataFrame({
    "Name": ["Yash", "Pratik", "Rahul"],
    "Department": ["IT", "HR", "Finance"]
}, index=[101, 102, 103])

performance = pd.DataFrame({
    "Score": [85, 90, 78],
    "Rating": ["Good", "Excellent", "Average"]
}, index=[101, 102, 103])

result = employees.join(performance)

print(result)
