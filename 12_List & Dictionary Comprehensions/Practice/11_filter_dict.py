marks = {
    
    "Yash": 85,
    "Jayesh": 49,
    "Sauradh": 90,
    "Suyash": 57,
    "Pratik": 92,
    
}

passed = {
    name: mark
    for name, mark in marks.items()
    if mark >=60
}

print(passed)