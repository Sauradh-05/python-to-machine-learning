# Statistics Basics - Mean, Median, Mode, Variance & Standard Deviation

This repository covers the fundamentals of **Statistics using Python and NumPy**, focusing on understanding how data can be summarized, interpreted, and analysed.

Statistics is an important part of Data Science and Machine Learning because it helps us understand the structure of a dataset, identify patterns, measure variations, and make better decisions based on data.

In this practice, I explored two important areas of statistics: **Measures of Central Tendency** and **Measures of Spread**. Using a sample student marks dataset, I implemented different statistical calculations and explored how extreme values (outliers) can affect the results.

The main objective is not just to calculate statistical values but also to understand what each value represents and when it should be used while analysing real-world data.

## 📚 Programs Overview

The programs in this repository cover the following statistical concepts and their practical implementation in Python.

### 1. Mean (Average)

Mean represents the average value of a dataset. It is calculated by adding all the observations and dividing the total by the number of observations.

In this practice, I used NumPy's `np.mean()` function to calculate the average marks of students. I also explored how the mean represents the overall performance of a dataset and how extreme values can influence it.

### 2. Median

Median represents the middle value of a dataset after arranging all observations in ascending or descending order.

I used NumPy's `np.median()` function to calculate the median and understand why it is useful when working with datasets containing outliers or highly skewed values. Unlike the mean, the median is less affected by extreme observations.

### 3. Mode

Mode represents the value that occurs most frequently in a dataset.

Using Python's `multimode()` function from the `statistics` module, I practised identifying the most frequently occurring marks. This concept is useful when analysing repeated numerical values as well as categorical data, such as the most popular product or course.

### 4. Variance

Variance measures how much the observations in a dataset differ from the mean.

I used NumPy's `np.var()` function to calculate variance and understand how it represents the spread of data. I also explored the difference between population variance and sample variance using NumPy's `ddof` parameter.

A higher variance indicates that the values are more spread out, while a lower variance indicates that they are closer to the mean.

### 5. Standard Deviation

Standard deviation measures the amount of variation or dispersion in a dataset relative to its mean. It is calculated as the square root of variance.

Using NumPy's `np.std()` function, I calculated standard deviation and compared population and sample results. Since standard deviation is expressed in the same unit as the original data, it is often easier to interpret than variance.

### 6. Population vs Sample Statistics

Population statistics are calculated using the entire group of observations, whereas sample statistics are calculated using a smaller representative subset of a population.

In this practice, I compared population and sample variance and standard deviation using NumPy:

- `np.var(data)` - Population variance.
- `np.var(data, ddof=1)` - Sample variance.
- `np.std(data)` - Population standard deviation.
- `np.std(data, ddof=1)` - Sample standard deviation.

This helped me understand why the choice between population and sample calculations matters during statistical analysis.

### 7. Outlier Analysis - Understanding the Impact of Extreme Values

An outlier is a value that is significantly different from the other observations in a dataset.

To understand its impact, I compared student marks before and after introducing an unusually low score.

I calculated the mean and median for both datasets and observed how the extreme value affected the average while the median remained comparatively stable.

This practical comparison helped me understand why the median can be a better measure of central tendency for certain datasets.

## 🛠️ Technologies & Libraries Used

- **Python:** Used to implement statistical calculations and develop the practice programs.
- **NumPy:** Used for numerical operations and calculating mean, median, variance, and standard deviation.
- **Statistics:** Used to identify the mode of a dataset through Python's built-in `multimode()` function.

## ▶️ How to Run the Programs

Follow these steps to run the practice program on your local machine.

**Step 1: Clone the repository**

```bash
git clone <your-repository-link>
```

**Step 2: Navigate to the project directory**

```bash
cd Statistics-Basics
```

**Step 3: Install the required library**

```bash
pip install numpy
```

**Step 4: Run the Python program**

```bash
python statistics_basics.py
```

The program will calculate and display the statistical measures using the sample student marks dataset.

## 💡 Key Learnings

Through this practice, I developed an understanding of how statistical measures help describe and interpret datasets.

Some of the important concepts I learned include:

- Understanding the difference between measures of central tendency and measures of spread.
- Calculating mean, median, and mode using Python.
- Understanding when to use mean, median, or mode depending on the nature of the dataset.
- Measuring data variability using variance and standard deviation.
- Understanding the difference between population and sample statistics.
- Exploring how outliers influence the mean and median.
- Using Python and NumPy to perform statistical calculations on numerical datasets.

## 🎯 Why Statistics Matters in Machine Learning

Statistics provides the foundation for understanding data before applying Machine Learning algorithms.

Concepts such as mean, median, variance, and standard deviation are useful in Exploratory Data Analysis (EDA), identifying outliers, understanding data distributions, and preparing datasets for model training.

Having a good understanding of these concepts makes it easier to interpret datasets and understand how Machine Learning algorithms work with data.

## 🚀 What's Next?

This is one of the foundational steps in my Python and Machine Learning learning journey.

I plan to continue exploring more statistical concepts, including:

- Percentiles and Quartiles
- Interquartile Range (IQR)
- Outlier Detection
- Probability Basics
- Probability Distributions
- Correlation and Covariance
- Hypothesis Testing

---

**Part of my Python & Machine Learning Journey.**

Learning the concepts, implementing them in Python, and understanding how they are applied to real-world data.