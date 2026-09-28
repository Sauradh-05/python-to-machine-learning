try:
    a = int(input("Enter Numerator:"))
    b = int(input("Enter Denominator:"))
    
    print("Result:", a/b)
    
except ValueError:
    print("Enter integer only")
    
except ZeroDivisionError:
    print("Denominator cannot be zero")