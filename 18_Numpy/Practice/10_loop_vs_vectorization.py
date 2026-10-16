import numpy as np

numbers = np.array([1, 2, 3, 4, 5])

# Using loop
loop_result = []

for number in numbers:
    loop_result.append(number * 2)

print("Using Loop:", loop_result)

# Using NumPy
vectorized_result = numbers * 2

print("Using Vectorization:", vectorized_result)