student = {"name": "Yash", "age": 26}

try:
    key = input("Enter a key:")
    print(student[key])
except KeyError:
    print("That key does not exist.")