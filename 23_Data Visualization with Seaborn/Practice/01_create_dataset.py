
import pandas as pd

data = {
    "Student": ["A", "B", "C", "D", "E", "F",
                "G", "H", "I", "J"],
    "Study_Hours": [2, 5, 3, 8, 6, 4, 9, 7, 3, 6],
    "Attendance": [65, 85, 70, 95, 88, 75, 98, 90, 68, 86],
    "Assignment_Score": [60, 80, 65, 95, 85, 72, 98, 90, 62, 84],
    "Exam_Score": [55, 78, 60, 96, 82, 70, 99, 88, 58, 80],
    "Department": [
        "CS", "IT", "CS", "IT", "CS",
        "IT", "CS", "IT", "CS", "IT"
    ]
}

df = pd.DataFrame(data)

df.to_csv("student_performance.csv", index=False)

print(df)
print("\nDataset created successfully!")
