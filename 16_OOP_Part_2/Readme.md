# OOP Part 2 – Inheritance, Polymorphism & Encapsulation

This repository contains beginner-friendly Python practice programs covering three important Object-Oriented Programming concepts: **Inheritance, Polymorphism, and Encapsulation**.

The programs are arranged in a simple learning order, starting with basic inheritance and gradually moving toward polymorphism, encapsulation, and a combined OOP example.

## 📚 Programs Overview

### 1. Basic Inheritance

**File:** `01_basic_inheritance.py`

**Learn:** Understand how a child class can inherit methods from a parent class.

**Practice:** Create an `Animal` class and inherit it into a `Dog` class.

---

### 2. Single Inheritance

**File:** `02_single_inheritance.py`

**Learn:** Understand the relationship between a parent class and a child class.

**Practice:** Create a `Person` class and inherit it into a `Student` class.

---

### 3. Multilevel Inheritance

**File:** `03_multilevel_inheritance.py`

**Learn:** Understand inheritance across multiple levels.

**Practice:** Create `Animal`, `Dog`, and `Puppy` classes.

---

### 4. Multiple Inheritance

**File:** `04_multiple_inheritance.py`

**Learn:** Understand how a class can inherit from multiple parent classes.

**Practice:** Create `Father`, `Mother`, and `Child` classes.

---

### 5. Method Overriding

**File:** `05_method_overriding.py`

**Learn:** Understand how a child class can provide its own implementation of a parent method.

**Practice:** Override the `sound()` method in an `Animal` and `Dog` class.

---

### 6. Polymorphism with Different Classes

**File:** `06_polymorphism_classes.py`

**Learn:** Understand how the same method can behave differently for different objects.

**Practice:** Create `Dog`, `Cat`, and `Cow` classes with a common `sound()` method.

---

### 7. Polymorphism with Functions

**File:** `07_polymorphism_function.py`

**Learn:** Understand how one function can work with objects of different classes.

**Practice:** Create a `make_speak()` function that works with different animal objects.

---

### 8. Operator Overloading

**File:** `08_operator_overloading.py`

**Learn:** Understand how special methods can customize operators for objects.

**Practice:** Overload the `+` operator for a `Point` class using `__add__()`.

---

### 9. Public Attributes

**File:** `09_public_attributes.py`

**Learn:** Understand public attributes and how they can be accessed and modified directly.

**Practice:** Create a `Student` class with a public `name` attribute.

---

### 10. Protected Attributes

**File:** `10_protected_attributes.py`

**Learn:** Understand the convention of using a single underscore for attributes intended for internal or subclass use.

**Practice:** Create an `Employee` class with a `_salary` attribute.

---

### 11. Private Attributes

**File:** `11_private_attributes.py`

**Learn:** Understand private attributes using double underscores and Python's name-mangling behavior.

**Practice:** Create a `BankAccount` class with a private `__balance` attribute.

---

### 12. Getter and Setter Methods

**File:** `12_getter_setter.py`

**Learn:** Understand how getter and setter methods can provide controlled access to data.

**Practice:** Create methods to safely read and update student marks.

---

### 13. Property Decorator

**File:** `13_property_decorator.py`

**Learn:** Use `@property` to create controlled access to attributes with a cleaner syntax.

**Practice:** Create a `Student` class with a property for marks.

---

### 14. Bank Account

**File:** `14_bank_account.py`

**Learn:** Apply encapsulation to a practical real-world example.

**Practice:** Create a bank account with private balance, deposit, withdrawal, and balance methods.

---

### 15. Combined OOP Example

**File:** `15_combined_oop.py`

**Learn:** Combine inheritance, polymorphism, and encapsulation in one program.

**Practice:** Build a simple employee system with `Employee`, `Developer`, and `Designer` classes.

---

## 🧠 Concepts Covered

### Inheritance

- Basic inheritance
- Single inheritance
- Multilevel inheritance
- Multiple inheritance
- Method overriding

### Polymorphism

- Method overriding
- Polymorphism with different classes
- Duck typing
- Operator overloading
- Special methods

### Encapsulation

- Public attributes
- Protected attributes
- Private attributes
- Getter methods
- Setter methods
- `@property` decorator
- Data validation

## 🎯 Learning Objective

The goal of this practice set is to understand how Python OOP can be used to create code that is reusable, flexible, and easier to maintain.

After completing these programs, the next step is to explore more advanced OOP concepts and apply them in practical Python projects.

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming

## ▶️ How to Run

Clone or download the repository and run any Python file:

```bash
python 01_basic_inheritance.py
```

You can replace the filename with any of the programs in this repository.

## 📈 Learning Journey

This repository is part of my **Python & Machine Learning Journey**, where I am learning Python concepts step by step and practicing each topic through hands-on coding.

**Previous:** OOP Part 1 – Classes & Objects

**Current:** OOP Part 2 – Inheritance, Polymorphism & Encapsulation

**Next:** Advanced Python OOP concepts and practical applications.