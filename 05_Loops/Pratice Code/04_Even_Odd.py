n = int(input("Enter a Number:"))

print("Even Number:")
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)
 
print("Odd Number:")
for i in range(1, n+1):
    if i % 2 != 0:
        print(i)          