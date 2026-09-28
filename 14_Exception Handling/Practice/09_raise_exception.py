try:
    number = int(input("Enter a positive number:"))
    if number < 0:
        raise ValueError("Number cannot be negative")

except ValueError as error:
    print("Error", error)

else:
    print("Accepted", number)
     