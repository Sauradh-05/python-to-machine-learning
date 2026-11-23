
import numpy as np
from scipy import stats

# ----------------------------------
# 1. Two Independent Groups
# ----------------------------------

class_a = np.array([
    55, 60, 65, 70, 75,
    80, 85, 90, 62, 68
])

class_b = np.array([
    65, 67, 69, 70, 71,
    72, 73, 74, 76, 78
])

# ----------------------------------
# 2. Calculate Mean and Variance
# ----------------------------------

print("Class A Mean:", np.mean(class_a))
print("Class B Mean:", np.mean(class_b))

print("Class A Variance:", np.var(class_a, ddof=1))
print("Class B Variance:", np.var(class_b, ddof=1))

# ----------------------------------
# 3. Define Significance Level
# ----------------------------------

alpha = 0.05

# ----------------------------------
# 4. Perform Welch's T-Test
# ----------------------------------

t_statistic, p_value = stats.ttest_ind(
    class_a,
    class_b,
    equal_var=False
)

print("\nT-Statistic:", t_statistic)
print("P-Value:", p_value)

# ----------------------------------
# 5. Interpret Results
# ----------------------------------

if p_value < alpha:
    print("\nReject the Null Hypothesis.")
    print("The average scores are significantly different.")
else:
    print("\nFail to Reject the Null Hypothesis.")
    print("Insufficient evidence of a difference.")
