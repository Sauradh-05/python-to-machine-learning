
import numpy as np
from scipy import stats

# ----------------------------------
# 1. Dataset
# ----------------------------------

before = np.array([
    50, 55, 60, 58, 62,
    57, 54, 59, 61, 56
])

after = np.array([
    65, 68, 70, 66, 72,
    67, 64, 69, 71, 68
])

# ----------------------------------
# 2. Descriptive Statistics
# ----------------------------------

print("Before Training Mean:", np.mean(before))
print("After Training Mean:", np.mean(after))

improvement = after - before

print("Average Improvement:", np.mean(improvement))

# ----------------------------------
# 3. Hypothesis Formulation
# ----------------------------------

# H0: Training does not improve average scores.
# H1: Training improves average scores.

alpha = 0.05

# ----------------------------------
# 4. Perform One-Sided Paired T-Test
# ----------------------------------

t_statistic, p_value = stats.ttest_rel(
    after,
    before,
    alternative="greater"
)

print("\nT-Statistic:", t_statistic)
print("P-Value:", p_value)

# ----------------------------------
# 5. Statistical Decision
# ----------------------------------

if p_value < alpha:
    print("\nReject the Null Hypothesis.")
    print("There is statistical evidence of improvement.")
else:
    print("\nFail to Reject the Null Hypothesis.")
    print("Insufficient evidence of improvement.")

# ----------------------------------
# 6. Final Summary
# ----------------------------------

print("\n----- Final Summary -----")
print("Before Mean:", np.mean(before))
print("After Mean:", np.mean(after))
print("Mean Improvement:", np.mean(improvement))
print("Significance Level:", alpha)
