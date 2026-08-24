text = input("Enter a string:")

count = 0

for char in text.lower():
    if char in "aeiou":
        count = count + 1

print("Number of vowels in the string:", count)