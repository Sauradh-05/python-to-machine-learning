from functools import reduce

numbers = [1,2,3,4,5]

squares = map(lambda x: x * x, numbers)

total = reduce(lambda x, y: x + y, squares)

print(total)               
               