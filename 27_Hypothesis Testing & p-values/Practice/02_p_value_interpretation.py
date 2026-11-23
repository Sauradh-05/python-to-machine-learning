
# ----------------------------------
# 1. Define Significance Level
# ----------------------------------

alpha = 0.05

# ----------------------------------
# 2. Different P-values
# ----------------------------------

p_values = [0.001, 0.02, 0.05, 0.08, 0.12]

# ----------------------------------
# 3. Interpret P-values
# ----------------------------------

for p_value in p_values:

    print("\nP-value:", p_value)

    if p_value < alpha:
        print("Decision: Reject the Null Hypothesis")
        print("Result: Statistically significant")
    else:
        print("Decision: Fail to Reject the Null Hypothesis")
        print("Result: Not statistically significant")
