class WeakPasswordError(Exception):
    pass

try:
    password = input("Enter a password: ")
    if len(password) < 8:
        raise WeakPasswordError("Password must have at least 8 characters.")
except WeakPasswordError as error:
    print("Error:", error)
else:
    print("Password length is valid.")