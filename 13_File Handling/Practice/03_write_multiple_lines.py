students = ["Yash", "Rohit", "Pratik"]

with open("Student.txt", "w") as file:
    for student in students:
        file.write(student + "\n")