from functools import reduce

numbers = [14, 12, 93, 84, 75]

largest = reduce(lambda x, y: x if x > y else y, numbers)

print(largest) 