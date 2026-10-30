import matplotlib.pyplot as plt

subjects = ['Python', 'Java', 'SQL', 'ML', 'Statistics']
marks = [85, 78, 90, 88, 75]

plt.bar(subjects, marks, color='green')

plt.title('Student Marks Comparison')
plt.xlabel('Subjects')
plt.ylabel('Marks')

plt.show()