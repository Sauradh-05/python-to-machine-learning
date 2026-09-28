# Exception Handling - Python

This section covers **Exception Handling in Python**, a fundamental concept used to handle runtime errors and prevent programs from terminating unexpectedly.

The programs are arranged in a simple learning order, starting with basic exception handling using `try` and `except`, followed by `else`, `finally`, common Python exceptions, raising exceptions, and creating custom exceptions.

## 📚 Programs Overview

### 1. Division by Zero

**File:** `01_division.py`

**Learn:**

* Using `try` and `except`
* Handling `ZeroDivisionError`
* Performing division safely

**Practice:** Write a program that divides two numbers and handles division by zero.

### 2. Handling Invalid Input

**File:** `02_value_error.py`

**Learn:**

* Handling `ValueError`
* Converting user input into integers
* Validating user input

**Practice:** Accept an integer from the user and handle invalid input.

### 3. Multiple Exceptions

**File:** `03_multiple_exceptions.py`

**Learn:**

* Using multiple `except` blocks
* Handling different exceptions separately
* Understanding `ValueError` and `ZeroDivisionError`

**Practice:** Create a division program that handles invalid numbers and division by zero.

### 4. Try, Except, and Else

**File:** `04_try_except_else.py`

**Learn:**

* Using the `else` block
* Executing code when no exception occurs
* Understanding the flow of exception handling

**Practice:** Display a success message when the user enters a valid number.

### 5. Finally Block

**File:** `05_finally.py`

**Learn:**

* Using the `finally` block
* Executing cleanup code
* Understanding how `finally` works with exceptions

**Practice:** Write a program that displays a completion message regardless of whether an exception occurs.

### 6. Handling IndexError

**File:** `06_index_error.py`

**Learn:**

* Understanding `IndexError`
* Accessing list elements using indexes
* Handling out-of-range indexes

**Practice:** Access a list element using an index entered by the user.

### 7. Handling KeyError

**File:** `07_key_error.py`

**Learn:**

* Understanding `KeyError`
* Accessing dictionary values
* Handling missing dictionary keys

**Practice:** Retrieve a value from a dictionary using a key entered by the user.

### 8. Handling TypeError

**File:** `08_type_error.py`

**Learn:**

* Understanding `TypeError`
* Identifying incompatible data types
* Handling invalid operations between different types

**Practice:** Handle a type error caused by combining a string and an integer.

### 9. Raising Exceptions

**File:** `09_raise_exception.py`

**Learn:**

* Using the `raise` keyword
* Raising built-in exceptions
* Validating input with custom conditions

**Practice:** Raise a `ValueError` when the user enters a negative number.

### 10. Custom Exceptions

**File:** `10_custom_exception.py`

**Learn:**

* Creating custom exception classes
* Inheriting from the `Exception` class
* Raising and handling custom exceptions

**Practice:** Create an `InvalidAgeError` exception to validate age requirements.

### 11. Password Validation

**File:** `11_password_validation.py`

**Learn:**

* Creating a custom `WeakPasswordError`
* Validating password length
* Handling application-specific errors

**Practice:** Raise a custom exception when a password contains fewer than eight characters.

### 12. File Handling Exceptions

**File:** `12_file_handling.py`

**Learn:**

* Handling `FileNotFoundError`
* Reading files using `open()`
* Using `try`, `except`, and `finally` with file operations

**Practice:** Read a text file and handle the situation when the file does not exist.

## 🛠️ Key Concepts Covered

* `try` and `except`
* `else` and `finally`
* Common Python exception types
* Multiple exception handling
* The `raise` keyword
* Creating custom exceptions
* Input validation
* File handling and error management

## 🎯 Learning Objectives

By completing these programs, you will be able to:

* Handle runtime errors without abruptly terminating a program.
* Identify and handle common Python exceptions.
* Use `try`, `except`, `else`, and `finally` effectively.
* Raise built-in exceptions when conditions are not satisfied.
* Create custom exceptions for application-specific scenarios.
* Write more reliable, readable, and maintainable Python programs.

## ▶️ How to Run the Programs

1. Install Python on your system.
2. Clone or download this repository.
3. Open the project folder in your code editor or terminal.
4. Run any Python file using:

```bash
python 01_division.py
```

Replace `01_division.py` with the name of the program you want to execute.

## 🚀 What's Next?

After learning exception handling, I will continue exploring more Python concepts and applying them to practical programming problems as part of my **Python & Machine Learning Journey**.

---

⭐ If you find these programs helpful, feel free to explore the repository and practice along with me!
