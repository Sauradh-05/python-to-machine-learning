numbers = [10,25,33,48,55,66,75,80,92]

even = []
odd = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print("Even Numbers:", even)
print("Odd Numbers:", odd)  
