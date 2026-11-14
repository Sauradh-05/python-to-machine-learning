import numpy as np
from statistics import multimode


# 1. Sample Dataset

marks = [45, 48, 50, 52, 52, 55, 58, 60, 62, 65, 5]

data = np.array(marks)

print("Student Marks:", data)


# 2. Mean

mean_value = np.mean(data)

print("\nMean:", mean_value)

# 3. Median

median_value = np.median(data)

print("Median:", median_value)

# 4. Mode

mode_value = multimode(marks)

print("Mode:", mode_value)


# 5. Variance

population_variance = np.var(data)

sample_variance = np.var(data, ddof=1)

print("Population Variance:", population_variance)
print("Sample Variance:", sample_variance)

# 6. Standard Deviation

population_std = np.std(data)

sample_std = np.std(data, ddof=1)

print("Population Standard Deviation:", population_std)
print("Sample Standard Deviation:", sample_std)

# 7. Understanding Outliers

normal_marks = np.array([45, 48, 50, 52, 52, 55, 58, 60, 62, 65])

print("\n ---Outlier Comparison---")

print("Without Outlier:")
print("Mean:", np.mean(normal_marks))
print("Median:", np.median(normal_marks))

print("\nWith Outlier:")
print("Mean:", np.mean(data))
print("Median:", np.median(data))
