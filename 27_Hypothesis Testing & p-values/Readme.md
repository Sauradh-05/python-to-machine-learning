# Hypothesis Testing & p-values 

This repository covers the fundamentals of **Hypothesis Testing using Python, NumPy, and SciPy**.

Hypothesis testing is a statistical method used to evaluate assumptions, compare groups, and determine whether an observed difference is statistically significant or could reasonably occur due to random variation.

In this practice, I explore how hypothesis testing works through real-world examples based on student performance and employee training results. The programs focus on formulating hypotheses, interpreting p-values, understanding significance levels, and performing different types of t-tests using Python.

The objective is to understand how statistical methods help us evaluate claims and make decisions based on data rather than assumptions.

## 📚 Topics Covered

### 1. Null Hypothesis and Alternative Hypothesis

Understand the two competing statements used in hypothesis testing and how they help define a statistical problem before conducting an experiment.

- **Null Hypothesis (H₀):** Assumes that there is no significant difference or effect in the population being studied.
- **Alternative Hypothesis (H₁):** Suggests that a difference or effect exists.

The practice uses a student marks dataset to understand how hypotheses can be formulated around a claimed average score.

### 2. p-value Interpretation

Learn how p-values help evaluate the evidence against the null hypothesis.

A p-value represents the probability of observing results at least as extreme as the obtained results, assuming the null hypothesis is true and the statistical test assumptions hold.

The programs demonstrate how different p-values are interpreted using a significance level of 0.05.

- When p-value < 0.05, reject the null hypothesis.
- When p-value ≥ 0.05, fail to reject the null hypothesis.

The practice also explains why a p-value does not represent the probability that a hypothesis is true.

### 3. Significance Level (α)

Understand the role of the significance level in statistical decision-making.

The significance level is the threshold selected before performing a hypothesis test. A value of 0.05 is commonly used, meaning that the test is conducted with a 5% Type I error threshold under the null hypothesis.

### 4. One-Sample t-test

Learn how to compare the mean of a sample against a specified population value.

The practice uses student examination marks to check whether the average score is significantly different from a claimed average of 70.

It covers sample mean calculation, t-statistic calculation, p-value interpretation, and statistical decision-making using `scipy.stats.ttest_1samp()`.

### 5. Independent Two-Sample t-test

Understand how to compare the average values of two independent groups.

The example compares examination marks from students taught using traditional and new teaching methods.

The objective is to determine whether the observed difference between the two groups provides sufficient statistical evidence of a difference in their population means.

The test is implemented using `scipy.stats.ttest_ind()`.

### 6. Paired t-test

Learn how to compare two related sets of measurements collected from the same individuals.

The practice uses student marks recorded before and after a training programme to evaluate whether their average performance has changed.

It covers paired observations, average improvement, t-statistic calculation, and p-value interpretation using `scipy.stats.ttest_rel()`.

### 7. Welch's t-test

Understand how to compare the means of two independent groups without assuming that their population variances are equal.

The practice compares examination scores from two classes with different score distributions.

Welch's t-test is performed using `scipy.stats.ttest_ind()` with `equal_var=False`.

### 8. Complete Hypothesis Testing Practice

Apply the concepts together through an employee training example.

The program compares assessment scores before and after training, calculates average improvement, formulates hypotheses, performs a one-sided paired t-test, and interprets the statistical results.

This exercise brings together descriptive statistics, hypothesis formulation, t-tests, p-values, and statistical decision-making in one workflow.

## 📂 Programs Overview

### 01. Null vs Alternative Hypothesis

**File:** `01_null_vs_alternative_hypothesis.py`

Introduces hypothesis formulation using a student examination dataset. Calculates the sample mean and sample size, defines the null hypothesis and alternative hypothesis, and establishes the significance level before conducting a statistical test.

### 02. p-value Interpretation

**File:** `02_p_value_interpretation.py`

Practises interpreting different p-values using a significance level of 0.05. Demonstrates how to distinguish statistically significant results from results that do not provide sufficient evidence to reject the null hypothesis.

### 03. One-Sample t-test

**File:** `03_one_sample_ttest.py`

Compares the average marks of a student sample against a specified population mean of 70. Performs a one-sample t-test and interprets the t-statistic and p-value to evaluate whether the sample provides evidence of a difference.

### 04. Independent Two-Sample t-test

**File:** `04_independent_two_sample_ttest.py`

Compares examination scores from two independent student groups using different teaching methods. Calculates both group means, performs an independent two-sample t-test, and evaluates whether the difference between the groups is statistically significant.

### 05. Paired t-test

**File:** `05_paired_ttest.py`

Compares students' examination scores before and after a training programme. Uses a paired t-test to evaluate whether the average change in marks is statistically significant while accounting for the relationship between the two measurements.

### 06. Welch's t-test

**File:** `06_welch_ttest.py`

Compares examination scores from two independent classes without assuming equal population variances. Calculates group means and sample variances, performs Welch's t-test, and interprets the resulting p-value.

### 07. Complete Hypothesis Testing Practice

**File:** `07_hypothesis_testing_practice.py`

Combines the major concepts of hypothesis testing in an employee training example. Compares assessment scores before and after training, calculates average improvement, performs a one-sided paired t-test, and evaluates whether there is statistical evidence of improvement.

## 🛠️ Libraries Used

- **Python** – Implements statistical concepts and decision-making logic.
- **NumPy** – Creates sample datasets and calculates descriptive statistics such as mean and variance.
- **SciPy** – Performs statistical tests, calculates t-statistics and p-values, and supports hypothesis testing.

## 📌 Statistical Tests Summary

| Statistical Test | Purpose | Python Function |
|---|---|---|
| One-Sample t-test | Compare one sample mean against a specified value | `stats.ttest_1samp()` |
| Independent Two-Sample t-test | Compare two independent group means | `stats.ttest_ind()` |
| Paired t-test | Compare two related measurements | `stats.ttest_rel()` |
| Welch's t-test | Compare two independent means without assuming equal variances | `stats.ttest_ind(equal_var=False)` |

## 🎯 Learning Objectives

Through these practice programs, I aim to understand how to:

- Formulate null and alternative hypotheses.
- Understand the meaning and interpretation of p-values.
- Apply significance levels in statistical decision-making.
- Understand the role of t-statistics in hypothesis testing.
- Perform one-sample, independent two-sample, and paired t-tests.
- Understand when to use Welch's t-test.
- Compare group averages and evaluate statistical differences.
- Interpret statistical test results using Python.
- Distinguish statistical significance from practical significance.

## ▶️ How to Run

**1. Clone the repository**

```bash
git clone https://github.com/your-username/Hypothesis-Testing-p-values.git
```

**2. Navigate to the project folder**

```bash
cd Hypothesis-Testing-p-values
```

**3. Install the required libraries**

```bash
pip install -r requirements.txt
```

**4. Run an individual Python program**

```bash
python 01_null_vs_alternative_hypothesis.py
```

You can run the remaining programs individually by replacing the filename with the program you want to practise.

## 📦 Requirements

Create a `requirements.txt` file containing:

```text
numpy
scipy
```

## 📖 Key Takeaways

Hypothesis testing provides a structured way to evaluate assumptions and understand whether observed differences in data are statistically significant.

Through these exercises, I learned that selecting the correct statistical test is just as important as calculating the p-value. Understanding the relationship between hypotheses, sample data, significance levels, and statistical results helps us draw more meaningful conclusions.

This practice is part of my **Python & Machine Learning Journey**, where I am strengthening my Statistics foundation through practical Python implementations and real-world examples.

The goal is to build a clear understanding of statistical concepts that will be useful in Data Science, Machine Learning, and data-driven decision-making.
