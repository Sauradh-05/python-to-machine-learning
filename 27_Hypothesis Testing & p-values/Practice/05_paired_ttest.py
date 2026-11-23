
import numpy as np
from scipy import stats

# ----------------------------------
# 1. Student Marks Before Training
# ----------------------------------

before_training = np.array([
    55, 60, 58, 62, 65,
    57, 61, 59, 63, 56
])

# ----------------------------------
# 2. Student Marks After Training
# ----------------------------------

after_training = np.array([
    65, 68, 67, 70, 72,
    66, 69, 68, 71, 64
])

# ----------------------------------
# 3. Calculate Average Marks
# ----------------------------------

before_mean = np.mean(before_training)
after_mean = np.mean(after_training)

print("Average Before Training:", before_mean)
print("Average After Training:", after_mean)

# ----------------------------------
# 4. Define Hypotheses
# ----------------------------------

# H0: Mean paired difference = 0
# H1: Mean paired difference != 0

alpha = 0.05

# ----------------------------------
# 5. Perform Paired T-Test
# ----------------------------------

t_statistic, p_value = stats.ttest_rel(
    before_training,
    after_training
)

print("\nT-Statistic:", t_statistic)
print("P-Value:", p_value)

# ----------------------------------
# 6. Interpret Results
# ----------------------------------

if p_value < alpha:
    print("\nReject the Null Hypothesis.")
    print("There is a significant change in student marks.")
else:
    print("\nFail to Reject the Null Hypothesis.")
    print("Insufficient evidence of a change.")

# ----------------------------------
# 7. Calculate Improvement
# ----------------------------------

improvement = after_mean - before_mean

print("\nAverage Improvement:", improvement)
