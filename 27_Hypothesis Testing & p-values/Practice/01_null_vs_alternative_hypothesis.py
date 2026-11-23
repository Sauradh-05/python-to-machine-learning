
import numpy as np

# ----------------------------------
# 1. Student Marks Dataset
# ----------------------------------

marks = np.array([
    72, 68, 75, 80, 65,
    71, 69, 74, 77, 66,
    73, 70, 76, 68, 72
])

# ----------------------------------
# 2. Define Hypotheses
# ----------------------------------

# H0: Average student marks = 70
# H1: Average student marks != 70

population_mean = 70
alpha = 0.05

# ----------------------------------
# 3. Calculate Sample Statistics
# ----------------------------------

sample_mean = np.mean(marks)
sample_size = len(marks)

print("Sample Mean:", sample_mean)
print("Sample Size:", sample_size)

print("\nNull Hypothesis (H0): Mean = 70")
print("Alternative Hypothesis (H1): Mean != 70")
print("Significance Level:", alpha)
