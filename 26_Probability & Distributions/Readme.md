# Probability & Distributions

This repository covers the fundamentals of **Probability and Probability Distributions using Python**. It focuses on understanding how probability works, how data behaves under different distributions, and how mathematical concepts can be applied through practical programming.

Probability is an important part of Statistics, Data Science, and Machine Learning. It helps us understand uncertainty, estimate the likelihood of events, and make decisions based on available data. Probability distributions take this further by explaining how possible values of a random variable are spread and how frequently different outcomes can occur.

In this practice, I explored three commonly used probability distributions: **Normal Distribution, Binomial Distribution, and Uniform Distribution**. I used Python libraries such as NumPy, SciPy, and Matplotlib to generate random samples, calculate probabilities, analyse statistical properties, and visualise how each distribution behaves.

## 📚 Programs Overview

**01. Normal Distribution (01_normal_distribution.py)**

This program explores the Normal Distribution, which is commonly represented by a bell-shaped curve. I practised generating random values using a specified mean and standard deviation and examined how these two parameters influence the distribution. I also calculated the probability of values falling within a given range using the cumulative distribution function (CDF). Finally, I visualised the generated data using a histogram and compared it with the theoretical normal curve.

**02. Binomial Distribution (02_binomial_distribution.py)**

This program focuses on the Binomial Distribution, which is used to calculate the probability of a specific number of successes in a fixed number of independent trials. I used a coin-tossing example to understand how the number of trials and probability of success affect the results. I practised calculating the probability of getting exactly six heads in ten tosses using the probability mass function (PMF). I also generated random binomial samples and visualised the probability of different possible outcomes.

**03. Uniform Distribution (03_uniform_distribution.py)**

This program explores the Uniform Distribution, where every value has the same probability density within a specified continuous interval. I practised generating random values between a lower and upper limit and analysed their statistical properties, including the mean, minimum, and maximum. I also calculated the probability of a value falling within a particular range using the cumulative distribution function (CDF). A histogram was used to understand how the generated values are distributed across the interval.

**04. Compare Different Distributions (04_compare_distributions.py)**

This program brings together the three distributions to understand their differences in terms of shape, behaviour, and statistical properties. I generated separate random samples for Normal, Binomial, and Uniform distributions and visualised them using histograms. I also calculated and compared their mean and standard deviation to understand how each distribution represents data differently. This comparison helped me understand why selecting the appropriate probability distribution depends on the type of data and the problem being analysed.

## 📌 Key Concepts Covered

**1. Understanding Probability**

- Understanding probability as a measure of how likely an event is to occur.
- Identifying possible outcomes and events in random experiments.
- Understanding the difference between discrete and continuous random variables.
- Learning how probability helps describe uncertainty in data.

**2. Normal Distribution**

- Understanding the bell-shaped curve and its characteristics.
- Learning the role of mean and standard deviation.
- Understanding how data is distributed around the mean.
- Calculating probabilities using the Cumulative Distribution Function (CDF).
- Understanding the Probability Density Function (PDF).
- Visualising normal distributions using histograms and curves.

**3. Binomial Distribution**

- Understanding fixed numbers of independent trials.
- Identifying success and failure outcomes.
- Learning how the probability of success affects the distribution.
- Calculating the probability of exact outcomes using the Probability Mass Function (PMF).
- Generating binomial random samples.
- Visualising probabilities for different numbers of successes.

**4. Uniform Distribution**

- Understanding continuous uniform distributions.
- Learning how values are distributed across a specified interval.
- Generating uniformly distributed random samples.
- Calculating probabilities within a given range using CDF.
- Understanding the relationship between the interval and probability density.
- Visualising uniform distributions using histograms.

**5. Statistical Analysis and Visualisation**

- Calculating mean and standard deviation.
- Generating random samples using NumPy.
- Understanding theoretical and sample distributions.
- Comparing different distribution patterns.
- Creating histograms and probability curves using Matplotlib.

## 🛠️ Technologies & Libraries Used

- **Python:** Used to implement probability concepts and perform statistical calculations.
- **NumPy:** Used for numerical operations, random sampling, and generating data from different distributions.
- **SciPy:** Used to work with statistical distributions and calculate probabilities using PDF, PMF, and CDF functions.
- **Matplotlib:** Used to create histograms, distribution curves, and visual comparisons.

## ⚙️ Installation & Setup

**Step 1: Clone the repository**

```bash
git clone <your-repository-link>
```

**Step 2: Navigate to the project directory**

```bash
cd Probability-and-Distributions
```

**Step 3: Install the required libraries**

```bash
pip install numpy scipy matplotlib
```

**Step 4: Run the Python programs**

For example:

```bash
python 01_normal_distribution.py
```

You can run the remaining programs individually to explore each distribution.

## 📊 Why Probability Distributions Matter in Data Science & Machine Learning

Probability distributions are important because real-world data often contains uncertainty, variation, and randomness. Understanding how data behaves helps us choose appropriate statistical methods and build better analytical models.

In Data Science, probability distributions are useful for analysing datasets, understanding data patterns, identifying unusual observations, and performing statistical analysis.

In Machine Learning, they help us understand uncertainty, model random variables, work with probabilistic algorithms, and make predictions based on data.

Some practical applications include:

- **Data Analysis:** Understanding how values are spread across a dataset.
- **Statistical Inference:** Estimating population characteristics using sample data.
- **Anomaly Detection:** Identifying observations that are unusual compared to expected data behaviour.
- **Machine Learning:** Understanding probabilistic models and uncertainty in predictions.
- **Simulation:** Generating artificial data to test different scenarios and outcomes.
- **Decision Making:** Estimating the likelihood of events and making informed decisions.

## 🎯 Learning Outcomes

Through these practical programs, I developed a better understanding of how probability distributions work and how they can be implemented using Python.

I gained hands-on experience generating random samples, calculating probabilities, working with statistical functions, analysing distribution parameters, and visualising different data patterns.

Most importantly, I learned that Normal, Binomial, and Uniform distributions represent different types of random behaviour, and choosing the right distribution depends on the nature of the data and the problem being solved.

This practice has strengthened my understanding of Statistics and Probability, which will be useful as I continue learning Data Science and Machine Learning.

---

**Part of my Python & Machine Learning Journey.**