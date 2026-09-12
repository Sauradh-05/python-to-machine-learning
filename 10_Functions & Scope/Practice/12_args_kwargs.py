def display_data(*args, **kwargs):
    print("Positional Arguments:", args)
    print("Keyword Arguments:", kwargs)

display_data(
    10,
    20,
    30,
    name = "Sauradh",
    course = "Python"
)