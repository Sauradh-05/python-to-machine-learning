number = [10,20,30]

try:
    index = int(input("Enter an index(0-2)"))
    print(number[index])

except ValueError:
    print("Index must be an integer.")

except IndexError:
    print("Index is out of range.")     