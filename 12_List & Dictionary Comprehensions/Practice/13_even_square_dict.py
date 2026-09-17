numbers = range(1, 11)

even_squares = {
    n: n ** 2
    for n in numbers
    if n % 2 == 0
}

print(even_squares)