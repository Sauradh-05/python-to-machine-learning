# Python Lists - Python

A beginner-friendly collection of Python programs covering list creation, indexing, slicing, adding and removing elements, sorting, updating values, and basic list operations.

The programs are arranged in a simple learning order, starting with creating lists and gradually moving toward practical list-based programs.

## 📚 Programs Overview

### 01. Create List

**File:** `01_create_list.py`
**Learn:** Creating Lists
**Practice:** Create a list containing multiple values and display its elements.

### 02. List Indexing

**File:** `02_list_indexing.py`
**Learn:** List Indexing
**Practice:** Access individual elements from a list using positive and negative indexes.

### 03. List Slicing

**File:** `03_list_slicing.py`
**Learn:** List Slicing
**Practice:** Extract a portion of a list using start, stop, and step values.

### 04. List Append

**File:** `04_list_append.py`
**Learn:** `append()`
**Practice:** Add a new element to the end of a list using the `append()` method.

### 05. List Insert

**File:** `06_list_insert.py`
**Learn:** `insert()`
**Practice:** Insert a new element at a specific position in a list.

### 06. List Remove

**File:** `07_list_remove.py`
**Learn:** `remove()`
**Practice:** Remove a specific element from a list using the `remove()` method.

### 07. List Pop

**File:** `08_list_pop.py`
**Learn:** `pop()`
**Practice:** Remove and return an element from a list using the `pop()` method.

### 08. List Sort

**File:** `09_list_sort.py`
**Learn:** `sort()`
**Practice:** Arrange list elements in ascending order.

### 09. List Sort Descending

**File:** `10_list_sort_desc.py`
**Learn:** Descending Sorting
**Practice:** Arrange list elements in descending order.

### 10. Update List

**File:** `11_update_list.py`
**Learn:** Updating List Elements
**Practice:** Modify existing elements in a list using their indexes.

### 11. Minimum & Maximum

**File:** `12_min_max_list.py`
**Learn:** `min()` & `max()`
**Practice:** Find the smallest and largest values from a list.

### 12. List Sum & Average

**File:** `13_list_sum_average.py`
**Learn:** `sum()` & `len()`
**Practice:** Calculate the total and average of numerical values in a list.

### 13. Even & Odd List

**File:** `14_even_odd_list.py`
**Learn:** List Traversal & Conditions
**Practice:** Identify even and odd numbers from a list.

### 14. Count Elements

**File:** `15_count_elements.py`
**Learn:** Counting List Elements
**Practice:** Count elements or occurrences of values in a list.

### 15. List Squares

**File:** `16_list_squares.py`
**Learn:** List Processing
**Practice:** Create a new list containing the squares of numbers from an existing list.

## 🎯 Learning Objectives

After completing these programs, you should be able to:

* Create and store multiple values in Python lists.
* Access elements using positive and negative indexing.
* Extract elements using list slicing.
* Add elements using `append()` and `insert()`.
* Remove elements using `remove()` and `pop()`.
* Update existing list elements.
* Sort lists in ascending and descending order.
* Find minimum and maximum values.
* Calculate the sum and average of list elements.
* Identify even and odd numbers.
* Count elements in a list.
* Process list values to create new lists.

## 🧠 Concepts Covered

### Lists

Lists are used to store multiple values in a single variable.

```python
numbers = [10, 20, 30, 40, 50]
names = ["Rahul", "Amit", "Yash"]
```

### List Indexing

Access individual elements using their index.

```python
numbers = [10, 20, 30, 40]

print(numbers[0])
print(numbers[-1])
```

### List Slicing

Extract a portion of a list.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

### Adding Elements

```python
numbers.append(60)
numbers.insert(1, 15)
```

### Removing Elements

```python
numbers.remove(30)
numbers.pop()
```

### Sorting Lists

```python
numbers.sort()
numbers.sort(reverse=True)
```

### Updating Elements

```python
numbers[0] = 100
```

### Useful List Functions & Methods

```text
len()          → Number of elements
min()          → Smallest value
max()          → Largest value
sum()          → Total of numerical values
append()       → Add element at the end
insert()       → Add element at a specific position
remove()       → Remove a specific element
pop()          → Remove an element by index
sort()         → Sort the list
```

## ▶️ How to Run

Make sure Python is installed on your system.

Open the **07-Python-Lists** folder in your terminal and run any program:

```bash
python 01_create_list.py
```

For example:

```bash
python 13_list_sum_average.py
```

You can also run these programs using **VS Code, PyCharm**, or another Python-compatible editor.

## 📌 Recommended Learning Order

Follow the programs in numerical order:

```text
Create List
    ↓
List Indexing
    ↓
List Slicing
    ↓
Adding Elements
    ↓
Removing Elements
    ↓
Updating Elements
    ↓
Sorting
    ↓
List Functions & Methods
    ↓
List Processing
    ↓
Practical Programs
```

## 🏆 Practice Recommendation

For each program:

1. Understand what the program is doing.
2. Run it with different inputs.
3. Observe how the list changes.
4. Try modifying the list yourself.
5. Rewrite the program without looking at the solution.
6. Add one extra feature to the program.
7. Create a similar list problem on your own.

## 🔗 Next Topic

**Python Tuples & Sets**

After completing Python Lists, the next step is to learn **Tuples and Sets** and understand how they differ from lists.

```text
Python Lists
      ↓
Tuples & Sets
      ↓
Dictionaries
      ↓
Functions
      ↓
Object-Oriented Programming
      ↓
Data Structures
      ↓
Machine Learning
```

## 📖 Part of the Python Learning Journey

This folder is part of a structured **Python & Machine Learning Journey**, where concepts are learned progressively through theory, examples, and practical programs.

