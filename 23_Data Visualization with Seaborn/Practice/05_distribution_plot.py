
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance.csv")

# Histogram with KDE curve
sns.histplot(
    data=df,
    x="Exam_Score",
    bins=5,
    kde=True,
    color="steelblue"
)

plt.title("Distribution of Exam Scores")
plt.xlabel("Exam Score")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.show()
