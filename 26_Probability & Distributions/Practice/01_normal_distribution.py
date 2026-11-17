import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 1. Define distribution parameters

mean = 70
std_dev = 10

# 2. Generate random data

np.random.seed(42)
data = np.random.normal(mean, std_dev, 1000)

# 3. Calculate statistics

print("Mean:", np.mean(data))
print("Standard Deviation:", np.std(data))

# 4. Calculate probability of a value

probability = norm.cdf(80, mean, std_dev) - norm.cdf(
    60, mean, std_dev
)

print("Probability between 60 and 80:", probability)

# 5. Visualise the distribution

x = np.linspace(30, 110, 500)
y = norm.pdf(x, mean, std_dev)

plt.hist(data, bins=30, density=True, alpha=0.6,
         label="Generated Data")
plt.plot(x, y, linewidth=2, label="Normal Curve")

plt.title("Normal Distribution")
plt.xlabel("Values")
plt.ylabel("Density")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
