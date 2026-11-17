import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# 1. Generate random samples

normal_data = np.random.normal(50, 10, 1000)

binomial_data = np.random.binomial(10, 0.5, 1000)

uniform_data = np.random.uniform(0, 100, 1000)

# 2. Create visualisations

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].hist(normal_data, bins=25, edgecolor="black")
axes[0].set_title("Normal Distribution")
axes[0].set_xlabel("Values")

axes[1].hist(binomial_data, bins=11, edgecolor="black")
axes[1].set_title("Binomial Distribution")
axes[1].set_xlabel("Number of Successes")

axes[2].hist(uniform_data, bins=25, edgecolor="black")
axes[2].set_title("Uniform Distribution")
axes[2].set_xlabel("Values")

for ax in axes:
    ax.set_ylabel("Frequency")
    ax.grid(alpha=0.2)

plt.tight_layout()
plt.show()

# 3. Compare mean and standard deviation

print("Normal Distribution")
print("Mean:", np.mean(normal_data))
print("Standard Deviation:", np.std(normal_data))

print("\nBinomial Distribution")
print("Mean:", np.mean(binomial_data))
print("Standard Deviation:", np.std(binomial_data))

print("\nUniform Distribution")
print("Mean:", np.mean(uniform_data))
print("Standard Deviation:", np.std(uniform_data))
