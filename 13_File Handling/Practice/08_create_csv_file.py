import csv

student = [
    ["Name", "marks"],
    ["Yash", 90],
    ["Rohit", 85],
    ["Pratik", 95],
    ["Suyash", 80]
]

with open("Student.csv", "w", newline = "") as file:
    
   writer = csv.writer(file)
   writer.writerows(student)
   
print("CSV file Created Successfully.")
   