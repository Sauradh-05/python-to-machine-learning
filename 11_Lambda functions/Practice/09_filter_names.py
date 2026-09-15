names = ["America", "India", "China", "Japan", "Germany", "France", "Africa"]

result = list(filter(lambda name: name.startswith("A"), names))

print(result)
