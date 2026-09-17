# List & Dictionary Comprehensions - Python

This section covers **List Comprehensions and Dictionary Comprehensions** in Python. You will learn how to create, filter, and transform data using concise and readable expressions.

The programs are arranged in a simple learning order, starting with basic List Comprehensions and gradually moving toward conditional comprehensions and practical Dictionary Comprehension problems.

## 📚 Programs Overview

### 1. List Squares

**File:** `01_list_squares.py`
**Learn:** Basic List Comprehension
**Practice:** Create a list containing the squares of numbers.

### 2. Even Numbers

**File:** `02_even_numbers.py`
**Learn:** Conditional List Comprehension
**Practice:** Create a list containing only even numbers.

### 3. Odd Numbers

**File:** `03_odd_numbers.py`
**Learn:** Filtering with Comprehensions
**Practice:** Create a list containing only odd numbers.

### 4. Uppercase Names

**File:** `04_uppercase_names.py`
**Learn:** Data Transformation
**Practice:** Convert a list of names into uppercase.

### 5. Filter Words

**File:** `05_filter_words.py`
**Learn:** Conditional Comprehension
**Practice:** Select words based on their length.

### 6. Even or Odd

**File:** `06_even_odd.py`
**Learn:** `if-else` in Comprehensions
**Practice:** Create a list that identifies numbers as Even or Odd.

### 7. List Cubes

**File:** `07_list_cubes.py`
**Learn:** Mathematical Expressions
**Practice:** Generate a list containing cubes of numbers.

### 8. Positive Numbers

**File:** `08_positive_numbers.py`
**Learn:** Filtering Data
**Practice:** Extract positive numbers from a list.

### 9. Dictionary Squares

**File:** `09_dict_squares.py`
**Learn:** Basic Dictionary Comprehension
**Practice:** Create a dictionary containing numbers and their squares.

### 10. Dictionary Cubes

**File:** `10_dict_cubes.py`
**Learn:** Key-Value Generation
**Practice:** Create a dictionary containing numbers and their cubes.

### 11. Filter Dictionary

**File:** `11_filter_dict.py`
**Learn:** Conditional Dictionary Comprehension
**Practice:** Filter students based on their marks.

### 12. Word Lengths

**File:** `12_word_lengths.py`
**Learn:** Dictionary Transformation
**Practice:** Create a dictionary containing words and their lengths.

### 13. Even Square Dictionary

**File:** `13_even_square_dict.py`
**Learn:** Conditional Dictionary Comprehension
**Practice:** Create a dictionary of even numbers and their squares.

### 14. Temperature Dictionary

**File:** `14_temperature_dict.py`
**Learn:** Data Transformation
**Practice:** Convert Celsius temperatures into Fahrenheit.

### 15. Word Frequency

**File:** `15_word_frequency.py`
**Learn:** Dictionary Comprehension and Filtering
**Practice:** Create a dictionary containing the frequency of unique words.

---

## 🔹 List Comprehension

List Comprehension provides a concise way to create a new list from an existing iterable.

### Basic Syntax

```python
[expression for item in iterable]
```

### Example

```python
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)
```

**Output:**

```text
[1, 4, 9, 16, 25]
```

### Conditional List Comprehension

```python
[expression for item in iterable if condition]
```

Example:

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)
```

**Output:**

```text
[2, 4, 6]
```

### `if-else` Comprehension

```python
[expression_if_true if condition else expression_if_false for item in iterable]
```

Example:

```python
numbers = [1, 2, 3, 4, 5]

result = ["Even" if number % 2 == 0 else "Odd" for number in numbers]

print(result)
```

---

## 🔹 Dictionary Comprehension

Dictionary Comprehension provides a concise way to create dictionaries using key-value expressions.

### Basic Syntax

```python
{key: value for item in iterable}
```

### Example

```python
numbers = [1, 2, 3, 4, 5]

squares = {number: number ** 2 for number in numbers}

print(squares)
```

**Output:**

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Conditional Dictionary Comprehension

```python
{key: value for item in iterable if condition}
```

Example:

```python
numbers = range(1, 11)

even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}

print(even_squares)
```

---

## 🔄 Comprehensions vs Regular Loops

The same operation can often be written using either a regular loop or a comprehension.

### Using a Regular Loop

```python
numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)
```

### Using List Comprehension

```python
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]
```

List Comprehension makes simple transformations more concise.

However, **regular loops are preferable when the logic becomes complex**, involves multiple operations, or becomes difficult to read.

### When to Use Comprehensions

Use comprehensions when:

* The operation is simple and straightforward.
* You are transforming existing data.
* You are filtering data.
* The resulting code remains easy to read.

Use regular loops when:

* The logic contains multiple steps.
* There are complex conditions.
* Debugging is required.
* The comprehension becomes difficult to understand.

> **Remember:** Shorter code is not always better code. **Readability comes first.**

---

## 🎯 Key Learning Outcomes

After completing these programs, you should be able to:

* Understand List Comprehension syntax.
* Create lists using comprehensions.
* Apply conditions while creating lists.
* Use `if-else` expressions in comprehensions.
* Understand Dictionary Comprehension syntax.
* Create dictionaries dynamically.
* Filter data using comprehensions.
* Transform data using comprehensions.
* Decide when to use comprehensions instead of regular loops.

---

## 🐍 Python & Machine Learning Journey

This project is part of my **Python & Machine Learning Journey**, where I am strengthening my Python fundamentals through practical coding and gradually progressing toward **Machine Learning**.

**Learn → Practice → Build → Repeat**
