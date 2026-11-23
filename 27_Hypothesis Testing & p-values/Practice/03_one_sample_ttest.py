
import numpy as np
from scipy import stats

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

# H0: Population mean = 70
# H1: Population mean != 70

population_mean = 70
alpha = 0.05

# ----------------------------------
# 3. Calculate Sample Mean
# ----------------------------------

sample_mean = np.mean(marks)

print("Sample Mean:", sample_mean)
print("Population Mean:", population_mean)

# ----------------------------------
# 4. Perform One-Sample T-Test
# ----------------------------------

t_statistic, p_value = stats.ttest_1samp(
    marks,
    population_mean
)

print("\nT-Statistic:", t_statistic)
print("P-Value:", p_value)

# ----------------------------------
# 5. Interpret Results
# ----------------------------------

if p_value < alpha:
    print("\nReject the Null Hypothesis.")
    print("Average marks are significantly different from 70.")
else:
    print("\nFail to Reject the Null Hypothesis.")
    print("Insufficient evidence that average marks differ from 70.")
