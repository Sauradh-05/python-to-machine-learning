import csv

with open ("Student.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        if int(row["marks"]) > 80:
            print(row["Name"], row["marks"])
            