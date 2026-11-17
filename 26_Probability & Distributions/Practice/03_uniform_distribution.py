import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

# 1. Define parameters

lower_limit = 0
upper_limit = 10

# 2. Generate random data

np.random.seed(42)

data = np.random.uniform(
    lower_limit, upper_limit, 1000
)

# 3. Calculate statistics

print("Mean:", np.mean(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))

# 4. Calculate probability between 2 and 7

probability = uniform.cdf(7, loc=0, scale=10) - \
              uniform.cdf(2, loc=0, scale=10)

print("Probability between 2 and 7:", probability)

# 5. Visualise the distribution

plt.hist(data, bins=20, density=True, alpha=0.6)

x = np.linspace(0, 10, 500)
y = uniform.pdf(x, loc=0, scale=10)

plt.plot(x, y, linewidth=2)

plt.title("Uniform Distribution")
plt.xlabel("Values")
plt.ylabel("Density")
plt.grid(alpha=0.3)
plt.show()
