
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance.csv")

# Create pairplot
sns.pairplot(
    df,
    vars=[
        "Study_Hours",
        "Attendance",
        "Assignment_Score",
        "Exam_Score"
    ],
    hue="Department",
    diag_kind="hist"
)

plt.suptitle(
    "Student Performance Pairplot",
    y=1.02
)

plt.show()
