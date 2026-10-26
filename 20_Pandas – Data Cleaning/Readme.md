# Pandas - Data Cleaning

This project covers essential data-cleaning techniques using Python Pandas. It focuses on handling missing values, removing duplicate records, and renaming columns.

The programs are arranged in a simple learning order, from checking missing data to applying multiple cleaning techniques in a mini project.

## 📚 Programs Overview

### 1. Check Missing Values
- **File:** `01_check_missing_values.py`
- **Learn:** Use `isnull()` and `isnull().sum()` to identify missing values.
- **Practice:** Find the column with the most missing values.

### 2. Fill Missing Values
- **File:** `02_fill_missing_values.py`
- **Learn:** Use `fillna()` and replace missing values with the mean or a specified value.
- **Practice:** Replace missing ages using the median.

### 3. Drop Missing Values
- **File:** `03_drop_missing_values.py`
- **Learn:** Use `dropna()` to remove rows containing missing values.
- **Practice:** Remove rows only when the name is missing.

### 4. Remove Duplicate Records
- **File:** `04_remove_duplicates.py`
- **Learn:** Use `duplicated()` and `drop_duplicates()` to identify and remove duplicates.
- **Practice:** Remove duplicates based on a specific column.

### 5. Rename Columns
- **File:** `05_rename_columns.py`
- **Learn:** Use `rename()` to create clear and consistent column names.
- **Practice:** Convert column names to lowercase and replace spaces with underscores.

### 6. Data Cleaning Mini Project
- **File:** `06_data_cleaning_project.py`
- **Learn:** Combine missing-value handling, duplicate removal, and column renaming in one workflow.
- **Practice:** Clean a student dataset and export the results to a CSV file.

## 🛠️ Technologies Used

- Python
- Pandas

## ⚙️ Installation

Install Pandas using pip:

```bash
pip install pandas
```

## ▶️ How to Run

Run any program from the terminal:

```bash
python 01_check_missing_values.py
```

Replace the filename with the program you want to execute.

## 🎯 Learning Outcomes

After completing these programs, you will understand how to:

- Identify and handle missing values.
- Remove duplicate records.
- Rename columns for better readability.
- Combine cleaning operations into a workflow.
- Export cleaned data to a CSV file.

## 🚀 Next Step

Apply these techniques to a real-world dataset and explore additional Pandas operations for data preprocessing.

---

**Part of my Python & Machine Learning Journey 🐍**
