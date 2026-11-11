
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance.csv")

# Select numerical columns
numeric_df = df.select_dtypes(include="number")

# Calculate correlation
correlation = numeric_df.corr()

# Create heatmap
sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5,
    fmt=".2f"
)

plt.title("Student Performance Correlation Heatmap")
plt.tight_layout()
plt.show()
