import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 150, 130, 200]

subjects = ["Python", "Java", "SQL"]
marks = [85, 75, 90]

study_hours = [1, 2, 3, 4, 5]
scores = [35, 45, 55, 70, 85]

student_marks = [45, 50, 60, 65, 70, 75, 80, 90]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Line plot
axes[0, 0].plot(months, sales, marker="o")
axes[0, 0].set_title("Monthly Sales")

# Bar plot
axes[0, 1].bar(subjects, marks)
axes[0, 1].set_title("Subject Marks")

# Scatter plot
axes[1, 0].scatter(study_hours, scores)
axes[1, 0].set_title("Study Hours vs Scores")

# Histogram
axes[1, 1].hist(student_marks, bins=5, edgecolor="black")
axes[1, 1].set_title("Marks Distribution")

fig.suptitle("Matplotlib Visualization Dashboard")
plt.tight_layout()
plt.show()