import csv

name = input("Enter the Name:")
marks = int(input("Enter the Marks:"))

with open("results.csv", "a", newline ="") as file:
    writer = csv.writer(file)
    
    writer.writerow([name, marks])
    
print("\n Student scoring 90 or above:")

with open ("results.csv", "r") as file:
    reader = csv.reader(file)
    
    for row in reader:
        if len(row) == 2 and row[1].isdigit():
            if int(row[1]) >= 90:
                print(f"{row[0]} - {row[1]}")
                