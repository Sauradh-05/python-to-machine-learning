marks = {
    "Maths" : 85,
    "Python" : 92,
    "English" : 78
    
}

highest_subject = max(marks, key=marks.get)

print("Highest Marks in:", highest_subject)
print("Marks:", marks[highest_subject]) 