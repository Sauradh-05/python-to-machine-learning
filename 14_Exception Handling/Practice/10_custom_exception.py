class InvalidAgeError(Exception):
      pass
  
try:
    age = int(input("Enter your age:"))
    
    if age < 18:
        raise InvalidAgeError("You must be at least 18")

except ValueError:
    print("Enter a valid age.")

except InvalidAgeError as error:
    print("Error:",error)

else:
    print("Access Granted.")