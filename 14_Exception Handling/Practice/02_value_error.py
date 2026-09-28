try:
    age = int(input("Enter your age"))
    print("your age is:", age)

except ValueError:
    print("Please enter a valid integer")
    