import matplotlib.pyplot as plt 

marks =[
    45, 50, 55, 60,62,
    65, 70, 75, 80, 85,
    78, 80, 82, 85, 90,
    92, 95, 88, 76, 69

]

plt.hist(
    marks,
    bins=5,
    color='purple',
    edgecolor='black'
)

plt.title('Distribution of Student Marks')
plt.xlabel('Marks')
plt.ylabel('Number of Students')

    
plt.show()    