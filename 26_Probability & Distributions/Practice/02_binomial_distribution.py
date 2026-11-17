import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# 1. Define parameters

n = 10
p = 0.5

# 2. Calculate probability of exactly 6 heads

probability = binom.pmf(6, n, p)

print("Probability of exactly 6 heads:", probability)

# 3. Generate random samples

np.random.seed(42)
data = np.random.binomial(n, p, 1000)

print("Average number of successes:", np.mean(data))

# 4. Calculate probabilities for all outcomes

x = np.arange(0, n + 1)
probabilities = binom.pmf(x, n, p)

# 5. Visualise the distribution

plt.bar(x, probabilities)

plt.title("Binomial Distribution")
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.xticks(x)
plt.grid(axis="y", alpha=0.3)
plt.show()
