minutes = int(input("Enter total Minutes:"))

hours = minutes // 60

remaining_minutes = minutes % 60

print(f"{minutes} minutes = {hours} Hours and {remaining_minutes} minutes")