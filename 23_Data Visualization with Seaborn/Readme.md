# Data Visualization – Seaborn

## 📖 Introduction

Data visualization plays an important role in understanding and analyzing datasets. Instead of looking at rows and columns of numbers, visualizations help us identify patterns, relationships, trends, and unusual values more easily.

In this section of my **Python & Machine Learning Journey**, I explored **Seaborn**, a Python library built on top of Matplotlib that makes statistical data visualization easier.

I practiced different types of visualizations using a Student Performance Dataset to understand how numerical features are related, how data is distributed, and how we can identify potential outliers.

The main focus of this practice is not just creating charts, but also understanding how to interpret them and extract meaningful information from data.

## 🎯 Learning Objectives

Through these programs, I focused on learning how to:

- Create statistical visualizations using Seaborn.
- Understand relationships between numerical variables.
- Identify correlations between different features.
- Explore data patterns using pairplots.
- Understand data distribution using boxplots and histograms.
- Identify potential outliers in a dataset.
- Choose appropriate visualizations for Exploratory Data Analysis (EDA).
- Understand the differences between Seaborn and Matplotlib.

## 📚 Programs Overview

This repository contains five Python programs. Each program focuses on a particular step in preparing and visualizing the Student Performance Dataset.

### 01. Create Dataset - `01_create_dataset.py`

Started by creating a sample Student Performance Dataset using Pandas.

The dataset contains information such as student study hours, attendance, assignment scores, exam scores, and department.

In this program, I practiced creating a Pandas DataFrame from dictionary data and exporting it into a CSV file using `to_csv()`.

This CSV file is then used as the common dataset for all the visualization programs.

### 02. Heatmap - `02_heatmap.py`

A heatmap is used to represent numerical values through different colours, making it easier to identify patterns in a dataset.

In this program, I calculated the correlation between numerical features using Pandas `corr()` and visualized the correlation matrix using Seaborn `heatmap()`.

I also explored:
- `annot=True` to display correlation values inside the heatmap.
- `cmap` to customize the colour scheme.
- `linewidths` to add spacing between cells.
- `fmt` to control the decimal format.

**What I learned:** How to identify positive and negative correlations between features and understand which numerical variables have stronger relationships.

### 03. Pairplot - `03_pairplot.py`

A pairplot helps visualize relationships between multiple numerical variables in a single figure.

In this program, I used Seaborn `pairplot()` to compare study hours, attendance, assignment scores, and exam scores.

I also used the `hue` parameter to distinguish students based on their department and `diag_kind` to display distributions along the diagonal.

**What I learned:** How to explore relationships between multiple features, identify possible patterns, and compare observations across different categories.

### 04. Boxplot - `04_boxplot.py`

A boxplot is useful for understanding how numerical data is distributed across different categories.

In this program, I created a boxplot to compare student exam scores between the CS and IT departments using Seaborn `boxplot()`.

I explored how a boxplot represents:
- Median – The middle value of the dataset.
- Quartiles – Values that divide the data into four equal parts.
- Interquartile Range (IQR) – The range between the first and third quartiles.
- Potential outliers – Values that fall beyond the usual whisker boundaries.

**What I learned:** How to compare distributions between categories, understand the spread of values, and identify potential outliers.

### 05. Distribution Plot - `05_distribution_plot.py`

A distribution plot helps understand how numerical values are spread across a dataset.

In this program, I used Seaborn `histplot()` to visualize the distribution of student exam scores.

I also explored:
- `bins` to divide values into intervals.
- `kde=True` to display a smooth density curve.
- `color` to customize the appearance of the plot.

**What I learned:** How to understand the frequency of values, identify where most observations are concentrated, and observe the overall shape of a distribution.

## 🛠️ Libraries and Tools Used

The following Python libraries were used throughout these exercises:

- **Python:** Programming language used to write the practice programs.
- **Pandas:** Used to create, manage, and analyze the dataset.
- **Matplotlib:** Used alongside Seaborn for plot customization and display.
- **Seaborn:** Used to create statistical visualizations and explore relationships within the dataset.

## ⚙️ Installation

Make sure Python is installed on your system.

Install the required libraries using pip:

```bash
pip install pandas matplotlib seaborn
```

## ▶️ How to Run the Programs

**Step 1: Clone the repository**

```bash
git clone <your-repository-url>
```

**Step 2: Navigate to the project directory**

```bash
cd Day-XX-Seaborn-Data-Visualization
```

**Step 3: Create the dataset**

Run the first program to generate the Student Performance CSV file.

```bash
python 01_create_dataset.py
```

**Step 4: Run the visualization programs**

After generating the CSV file, execute the remaining programs individually.

```bash
python 02_heatmap.py
python 03_pairplot.py
python 04_boxplot.py
python 05_distribution_plot.py
```

Each program generates a separate visualization window.

**Note:** All Python files should be executed from the same project directory because the visualization programs read `student_performance.csv` generated by the first program.

## 🔍 Seaborn vs Matplotlib

Both libraries are useful for data visualization, but they serve slightly different purposes.

**Matplotlib**
- Provides detailed control over plots and chart elements.
- Useful for creating customized visualizations.
- Offers flexibility in designing different types of charts.

**Seaborn**
- Makes statistical visualization easier with less code.
- Provides attractive default styles and colour palettes.
- Includes built-in functions for heatmaps, pairplots, boxplots, and distribution plots.

Seaborn is built on top of Matplotlib, so both libraries can also be used together.

## 💡 Key Takeaways

Through these exercises, I developed a better understanding of how visualizations can help in exploring and interpreting data.

Some important things I learned:

- A heatmap helps identify correlations between numerical features.
- A pairplot makes it easier to explore relationships between multiple variables.
- A boxplot helps compare distributions and detect potential outliers.
- A histogram helps understand the frequency and spread of numerical values.
- Selecting the right visualization makes data analysis easier and more meaningful.

Most importantly, I learned that creating a visualization is only the first step. Understanding what the chart represents and what insights we can draw from it is equally important.

## 🚀 What's Next?

With the basics of Pandas, Matplotlib, and Seaborn covered, the next step in my learning journey is to explore **Exploratory Data Analysis (EDA)** and apply these concepts to real-world datasets.

---

**Part of my Python & Machine Learning Journey.**