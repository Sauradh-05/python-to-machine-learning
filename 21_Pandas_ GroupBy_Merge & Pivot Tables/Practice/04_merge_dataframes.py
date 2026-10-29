
import pandas as pd

employees = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104],
    "Name": ["Yash", "Pratik", "Rahul", "Suyash"]
})

departments = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 105],
    "Department": ["IT", "HR", "Finance", "SAP"]
})

# Keep all employees and match available departments
result = pd.merge(
    employees,
    departments,
    on="Employee_ID",
    how="left"
)

print(result)
