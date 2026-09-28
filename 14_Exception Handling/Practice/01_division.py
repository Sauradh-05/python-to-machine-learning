try:
  a = float(input("Enter First Number:"))
  b = float(input("Enter Second Number"))
  
  print("Result:", a/b)
  
except ZeroDivisionError:
    print("Cannot divide by zero")