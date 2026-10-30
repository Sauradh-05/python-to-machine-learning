import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [35,40,50,55,65,70,80,90]

plt.scatter(
    study_hours,
    scores,
    color='red',
    marker='o',

)

plt.title('Study Hours vs Exam Scores')
plt.xlabel('Study Hours')
plt.ylabel('Exam Scores')
plt.grid(True)


plt.show()
