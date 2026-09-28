try:
    number = int(input("Enter a Number:"))
except ValueError:
    print("Invalid Number:")
    
else:
    print("You entered", number)
    print("No Excepttion occured:")