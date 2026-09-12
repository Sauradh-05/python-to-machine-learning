def student_info(**details):
    for key, value in details.items():
        print(key, ":", value)

student_info(
    name = "Sauradh",
    age = 26,
    course = "Python"
)