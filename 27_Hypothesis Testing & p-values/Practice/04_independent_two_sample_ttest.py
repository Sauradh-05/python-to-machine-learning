
import numpy as np
from scipy import stats

# ----------------------------------
# 1. Student Performance Data
# ----------------------------------

traditional_method = np.array([
    65, 68, 72, 70, 66,
    74, 69, 71, 63, 67
])

new_method = np.array([
    75, 78, 82, 80, 76,
    84, 79, 81, 73, 77
])

# ----------------------------------
# 2. Calculate Group Means
# ----------------------------------

traditional_mean = np.mean(traditional_method)
new_mean = np.mean(new_method)

print("Traditional Method Mean:", traditional_mean)
print("New Method Mean:", new_mean)

# ----------------------------------
# 3. Define Hypotheses
# ----------------------------------

# H0: Both groups have equal population means.
# H1: Both groups have different population means.

alpha = 0.05

# ----------------------------------
# 4. Perform Independent T-Test
# ----------------------------------

t_statistic, p_value = stats.ttest_ind(
    traditional_method,
    new_method,
    equal_var=False
)

print("\nT-Statistic:", t_statistic)
print("P-Value:", p_value)

# ----------------------------------
# 5. Interpret Results
# ----------------------------------

if p_value < alpha:
    print("\nReject the Null Hypothesis.")
    print("There is a significant difference between groups.")
else:
    print("\nFail to Reject the Null Hypothesis.")
    print("Insufficient evidence of a difference.")

# ----------------------------------
# 6. Calculate Mean Difference
# ----------------------------------

difference = new_mean - traditional_mean

print("\nMean Difference:", difference)
