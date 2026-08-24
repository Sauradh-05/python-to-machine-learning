text = input("Enter a string: ")
char = input("Enter a character:")

position = text.find(char)

if position != -1:
    print("Character found at index", position)
else:   
    print("Character not found")
    