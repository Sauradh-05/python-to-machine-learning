# Lambda, Map, Filter & Reduce – Python

A beginner-friendly collection of Python programs covering **Lambda Functions, `map()`, `filter()`, `reduce()`, and functional programming basics**.

The programs are arranged in a simple learning order, starting with anonymous functions and gradually moving toward practical data transformation, filtering, and aggregation.

## 📚 Programs Overview

### 01. Lambda Square

**File:** `01_lambda_square.py`
**Learn:** Creating anonymous functions using `lambda`
**Practice:** Calculate the square of a number.

### 02. Lambda Even Check

**File:** `02_lambda_even.py`
**Learn:** Lambda with conditions
**Practice:** Check whether a number is even.

### 03. Lambda Maximum

**File:** `03_lambda_max.py`
**Learn:** Lambda with built-in functions
**Practice:** Find the maximum value from a list.

### 04. Map Double

**File:** `04_map_double.py`
**Learn:** `map()` with lambda
**Practice:** Double every number in a list.

### 05. Map Square

**File:** `05_map_square.py`
**Learn:** Data transformation using `map()`
**Practice:** Generate squares of numbers.

### 06. Map Uppercase

**File:** `06_map_uppercase.py`
**Learn:** Applying functions to strings with `map()`
**Practice:** Convert a list of names to uppercase.

### 07. Filter Even Numbers

**File:** `07_filter_even.py`
**Learn:** Filtering data using `filter()`
**Practice:** Extract even numbers from a list.

### 08. Filter Greater Numbers

**File:** `08_filter_greater.py`
**Learn:** Conditional filtering
**Practice:** Find numbers greater than 10.

### 09. Filter Names

**File:** `09_filter_names.py`
**Learn:** Filtering strings
**Practice:** Find names starting with a specific letter.

### 10. Reduce Sum

**File:** `10_reduce_sum.py`
**Learn:** Aggregating values with `reduce()`
**Practice:** Calculate the sum of numbers.

### 11. Reduce Product

**File:** `11_reduce_product.py`
**Learn:** Repeated operations with `reduce()`
**Practice:** Calculate the product of numbers.

### 12. Reduce Maximum

**File:** `12_reduce_max.py`
**Learn:** Comparing values using `reduce()`
**Practice:** Find the largest number in a list.

### 13. Map & Filter

**File:** `13_map_filter.py`
**Learn:** Combining functional programming tools
**Practice:** Find the squares of even numbers.

### 14. Filter Marks

**File:** `14_filter_marks.py`
**Learn:** Filtering real-world data
**Practice:** Select passing marks from a list.

### 15. Map & Reduce

**File:** `15_map_reduce.py`
**Learn:** Combining `map()` and `reduce()`
**Practice:** Calculate the sum of squares.

---

## 🧠 Key Concepts Covered

* Anonymous functions
* `lambda` expressions
* Functional programming basics
* `map()`
* `filter()`
* `reduce()`
* `functools.reduce()`
* Data transformation
* Data filtering
* Data aggregation
* Combining functional programming tools

## 🔄 Quick Concept Guide

| Function   | Purpose                           | Example           |
| ---------- | --------------------------------- | ----------------- |
| `lambda`   | Create a small anonymous function | `lambda x: x * 2` |
| `map()`    | Transform every item              | Double numbers    |
| `filter()` | Select matching items             | Find even numbers |
| `reduce()` | Combine values into one result    | Calculate total   |

## 📁 Learning Flow

```text
Lambda
  ↓
map()
  ↓
filter()
  ↓
reduce()
  ↓
map() + filter()
  ↓
map() + reduce()
  ↓
Functional Programming Basics
```

## 🎯 Learning Goals

After completing these programs, you should be able to:

* Create simple anonymous functions using `lambda`.
* Apply transformations using `map()`.
* Filter collections using `filter()`.
* Perform cumulative operations using `reduce()`.
* Combine multiple functional programming techniques.
* Understand where functional programming can simplify Python code.
* Recognize when a normal function may be more readable than a lambda.

## 🚀 How to Run

Make sure Python is installed on your system.

Run any program using:

```bash
python filename.py
```

For example:

```bash
python 07_filter_even.py
```

## 🛠️ Requirements

* Python 3.x
* No external libraries required
* `functools` is used for `reduce()`, and it is included in Python's standard library.

## 📌 Note

Lambda functions are useful for **small, simple operations**, while regular `def` functions are generally better for complex logic and reusable functionality.

The goal of these programs is to understand the fundamentals of functional programming and learn how Python can process collections in a concise and expressive way.

---

### 📈 Python & Machine Learning Journey

This topic is part of my **Python & Machine Learning Journey**, where I am building my Python fundamentals step by step before moving deeper into **Data Science and Machine Learning**.

⭐ Feel free to explore the programs, practice them, and experiment with your own examples.
