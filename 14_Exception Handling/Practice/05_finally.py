try:
    number = int(input("Enter a Number:"))
    print("Number:",number)
except ValueError:
    print("Inavlid Input")
finally:
    print("Program execution completed.")    