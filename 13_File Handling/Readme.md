# 📂 File Handling in Python

This repository contains my learning and practice programs for **File Handling in Python** as part of my **Python & Machine Learning Journey**. 🐍🤖

File handling is an important Python concept used to **create, read, write, update, and manage files**. It is especially useful when working with datasets and real-world data.

---

## 📚 Topics Covered

* `open()` function
* File modes
* Reading files
* Writing files
* Appending data
* `with` statement
* Working with `.txt` files
* Working with `.csv` files
* `csv.reader()`
* `csv.writer()`
* `csv.DictReader()`
* Practical file-handling programs

---

## 🔓 `open()` Function

The `open()` function is used to open a file.

### Syntax

```python
open("filename", "mode")
```

### Example

```python
file = open("data.txt", "r")
```

It is recommended to use the `with` statement so that Python automatically closes the file.

---

## 📌 File Modes

| Mode | Description                                    |
| ---- | ---------------------------------------------- |
| `r`  | Read an existing file                          |
| `w`  | Write to a file and overwrite existing content |
| `a`  | Append data to the end of a file               |
| `x`  | Create a new file                              |
| `r+` | Read and write                                 |

### Example

```python
with open("data.txt", "w") as file:
    file.write("Hello Python!")
```

---

## 📖 Reading a Text File

### Using `read()`

```python
with open("data.txt", "r") as file:
    content = file.read()

print(content)
```

### Using `readlines()`

```python
with open("data.txt", "r") as file:
    lines = file.readlines()

print(lines)
```

### Reading Line by Line

```python
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())
```

---

## ✍️ Writing to a Text File

The `"w"` mode is used to write data.

```python
with open("students.txt", "w") as file:
    file.write("Rahul\n")
    file.write("Priya\n")
    file.write("Amit\n")
```

> ⚠️ **Note:** `"w"` mode overwrites the existing content of the file.

---

## ➕ Appending to a File

The `"a"` mode adds new content without removing existing data.

```python
with open("students.txt", "a") as file:
    file.write("Sneha\n")
```

---

## 🧹 Using the `with` Statement

The `with` statement automatically closes the file after the operation is completed.

```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

### Why use `with`?

* Automatically closes the file
* Cleaner code
* Safer file handling
* Recommended Python practice

---

# 📄 Working with `.txt` Files

Text files can be used to store simple textual information.

### Example

```python
with open("welcome.txt", "w") as file:
    file.write("Welcome to Python File Handling!")
```

Reading the file:

```python
with open("welcome.txt", "r") as file:
    print(file.read())
```

---

# 📊 Working with `.csv` Files

CSV stands for **Comma-Separated Values**.

CSV files are commonly used to store structured data such as:

* Student records
* Employee information
* Sales data
* Customer information
* Machine Learning datasets

Python provides the built-in `csv` module for working with CSV files.

---

## 📥 Reading a CSV File

```python
import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

### Example CSV

```text
Name,Marks
Rahul,85
Priya,92
Amit,78
```

---

## 📤 Writing to a CSV File

```python
import csv

students = [
    ["Name", "Marks"],
    ["Rahul", 85],
    ["Priya", 92],
    ["Amit", 78]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)
```

---

## 🔑 Using `DictReader`

`DictReader` allows us to access CSV data using column names.

```python
import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["Name"], row["Marks"])
```

---

# 🧪 Practice Programs

This repository also contains practice programs such as:

### Beginner

* Create and write to a text file
* Read a text file
* Write multiple lines
* Append data to a file

### Intermediate

* Count lines in a file
* Read a file line by line
* Count words in a file
* Read CSV data
* Write data to CSV
* Filter CSV records

### Challenge

**Student Result Manager**

The program:

1. Takes student name and marks as input
2. Stores the information in a CSV file
3. Reads the CSV file
4. Displays students scoring 90 or above

---

## 🎯 Learning Objectives

After completing these programs, I should be able to:

* Understand different file modes
* Create and manage text files
* Read and write file content
* Append information to existing files
* Use the `with` statement
* Work with CSV files
* Read structured data from CSV files
* Prepare basic data for further analysis

---

## 🛠️ Technologies Used

* 🐍 Python
* 📄 TXT Files
* 📊 CSV Files
* 🧰 Python `csv` Module

---

## 🚀 What's Next?

File handling is an important foundation for working with real-world data.

My next steps are to practice:

* Data cleaning
* Exception handling
* Pandas
* NumPy
* Data analysis
* Working with real-world datasets
* Machine Learning 🤖

---

## 📈 My Python & Machine Learning Journey

> **Learn → Practice → Build → Share → Improve 🚀**

Every small Python concept is another step toward becoming better at **Data Science and Machine Learning**.

---

## ⭐ If You Find This Useful

Feel free to explore the programs, practice them yourself, and experiment with the code.


