# Strings & String Methods - Python

A beginner-friendly collection of Python programs covering **strings, indexing, slicing, string methods, splitting, joining, string formatting, and basic text processing**.

The programs are arranged in a simple learning order, starting with basic string operations and gradually moving toward practical string manipulation programs.

## 📚 Programs Overview

### 01. First & Last Character

**File:** `01_string_first_last.py`
**Learn:** String Indexing
**Practice:** Access the first and last character of a string using positive and negative indexing.

### 02. Reverse String

**File:** `02_string_reverse.py`
**Learn:** String Slicing
**Practice:** Reverse a string using Python slicing.

### 03. String Length

**File:** `03_string_length.py`
**Learn:** `len()` Function
**Practice:** Find the total number of characters in a string.

### 04. Upper & Lower Case

**File:** `04_string_upper_lower.py`
**Learn:** `upper()` & `lower()`
**Practice:** Convert a string into uppercase and lowercase.

### 05. Strip Spaces

**File:** `05_string_strip.py`
**Learn:** `strip()` Method
**Practice:** Remove unnecessary spaces from the beginning and end of a string.

### 06. Count Vowels

**File:** `06_count_vowels.py`
**Learn:** String Iteration & Conditions
**Practice:** Count the number of vowels present in a string.

### 07. Count Words

**File:** `07_count_words.py`
**Learn:** `split()` Method
**Practice:** Split a sentence into words and count the total number of words.

### 08. Replace Word

**File:** `08_replace_word.py`
**Learn:** `replace()` Method
**Practice:** Replace a specific word or text with another value.

### 09. Check Palindrome

**File:** `09_check_palindrome.py`
**Learn:** Slicing & Conditions
**Practice:** Check whether a string reads the same forward and backward.

### 10. Count Character

**File:** `10_count_character.py`
**Learn:** `count()` Method
**Practice:** Count how many times a specific character appears in a string.

### 11. Find Character

**File:** `11_find_character.py`
**Learn:** `find()` Method
**Practice:** Find the position of a specific character in a string.

### 12. Join Words

**File:** `12_join_words.py`
**Learn:** `join()` & `split()`
**Practice:** Split a sentence into words and join them using a selected separator.

### 13. String Format

**File:** `13_string_format.py`
**Learn:** `.format()` Method
**Practice:** Insert variables into strings using the `format()` method.

### 14. f-String

**File:** `14_f_string.py`
**Learn:** f-Strings
**Practice:** Create formatted strings using Python f-string syntax.

### 15. Count String Types

**File:** `15_count_string_types.py`
**Learn:** String Methods & Conditions
**Practice:** Count vowels, consonants, digits, and spaces in a string.

### 16. Check Start & End

**File:** `16_check_start_end.py`
**Learn:** `startswith()` & `endswith()`
**Practice:** Check whether a string starts or ends with specific text.

### 17. Remove Duplicates

**File:** `17_remove_duplicates.py`
**Learn:** String Iteration
**Practice:** Remove duplicate characters while preserving their original order.

### 18. Longest Word

**File:** `18_longest_word.py`
**Learn:** `split()` & `len()`
**Practice:** Find the longest word from a given sentence.

### 19. Reverse Words

**File:** `19_reverse_words.py`
**Learn:** `split()`, Slicing & `join()`
**Practice:** Reverse each word in a sentence while maintaining the word order.

### 20. Username Generator

**File:** `20_username_generator.py`
**Learn:** String Methods & f-Strings
**Practice:** Generate a simple username using user information and string manipulation.

## 🎯 Learning Objectives

After completing these programs, you should be able to:

* Understand how strings work in Python.
* Access characters using string indexing.
* Extract text using string slicing.
* Find the length of a string using `len()`.
* Modify strings using common string methods.
* Split strings into individual words.
* Join multiple strings using a separator.
* Search and replace text within strings.
* Format strings using `.format()` and f-strings.
* Perform basic text-processing operations.
* Build simple real-world string-based programs.

## 🧠 Concepts Covered

### String Indexing

Indexing is used to access individual characters from a string.

```python
name = "Python"

print(name[0])
print(name[-1])
```

### String Slicing

Slicing is used to extract a portion of a string.

```python
text = "Python"

print(text[0:3])
print(text[::-1])
```

### Common String Methods

```text
upper()       → Convert text to uppercase
lower()       → Convert text to lowercase
strip()       → Remove leading and trailing spaces
replace()     → Replace text
count()       → Count occurrences
find()        → Find the position of text
split()       → Split a string into a list
join()        → Join elements into a string
startswith()  → Check the beginning of a string
endswith()    → Check the ending of a string
isalpha()     → Check whether characters are alphabetic
isdigit()     → Check whether characters are digits
```

### String Formatting

Using `.format()`:

```python
name = "Yash"
age = 21

print("My name is {} and I am {} years old.".format(name, age))
```

Using f-strings:

```python
name = "Yash"
age = 21

print(f"My name is {name} and I am {age} years old.")
```

### Split & Join

```python
text = "Python is easy"

words = text.split()
result = "-".join(words)

print(result)
```

## ▶️ How to Run

Make sure Python is installed on your system.

Open the `Day-07-Python-Strings` folder in your terminal and run any program:

```bash
python 01_string_first_last.py
```

For example:

```bash
python 20_username_generator.py
```

You can also run these programs using **VS Code, PyCharm, Jupyter Notebook**, or another Python-compatible editor.

## 📌 Recommended Learning Order

Follow the programs in numerical order:

```text
String Basics
     ↓
Indexing & Slicing
     ↓
Common String Methods
     ↓
split() & join()
     ↓
String Formatting
     ↓
String Processing
     ↓
Practical String Programs
```

## 🏆 Practice Recommendation

For each program:

* Understand what the program is doing.
* Run it with different inputs.
* Observe how the output changes.
* Try modifying the string and methods used.
* Rewrite the program without looking at the solution.
* Add one extra feature to the program.
* Create a similar string problem on your own.

## 🔗 Next Topic

**Python List**

After completing Strings & String Methods, the next step is to learn **Python List**, which are used to store and manage collections of multiple values.

```text
Strings & String Methods
        ↓
Lists
        ↓
Tuples & Sets
        ↓
Dictionaries
        ↓
Functions
        ↓
Object-Oriented Programming
        ↓
NumPy
        ↓
Pandas
        ↓
Machine Learning
```

## 📖 Part of the Python Learning Journey

This folder is part of a structured **Python & Machine Learning journey**, where concepts are learned progressively through theory, examples, and practical programs.

