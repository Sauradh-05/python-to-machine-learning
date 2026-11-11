
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance.csv")

sns.boxplot(
    data=df,
    x="Department",
    y="Exam_Score",
    hue="Department",
    palette="Set2",
    legend=False
)

plt.title("Exam Scores by Department")
plt.xlabel("Department")
plt.ylabel("Exam Score")

plt.tight_layout()
plt.show()
