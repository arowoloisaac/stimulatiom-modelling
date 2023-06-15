import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare

# Define PMF
# pmf = [0.1, 0.2, 0.3, 0.2, 0.1, 0.1]
n = int(input('Number of recursion: '))
# events = [event+1 for event in range(n+1)]

pmf = []

prob_sum = 0

for i in range(n):
    inp_prob = float(input(f'input the number {i+1} float: '))
    pmf.append(inp_prob)

    prob_sum = sum(pmf)

if prob_sum < 1:
   check_sum = 1 - prob_sum
   pmf.append(round(check_sum, 3))

elif prob_sum >= 1:
    if prob_sum == 1:
        pmf.append(0)

    else:
        print('Error')


else:
    print('not equal')
# Define number of trials
N = 10000

# Generate random numbers
random_nums = np.random.uniform(size=N)

# Find outcomes for each random number
outcomes = []
for num in random_nums:
    cumulative_prob = 0
    for i in range(len(pmf)):
        cumulative_prob += pmf[i]
        if num <= cumulative_prob:
            outcomes.append(i)
            break

# Calculate empirical probabilities
empirical_probs = []
for i in range(len(pmf)):
    empirical_probs.append(sum(1 for outcome in outcomes if outcome == i) / N)

# Calculate sample mean and variance

mean = sum(i * empirical_probs[i] for i in range(len(pmf)))
variance = sum((i - mean) ** 2 * empirical_probs[i] for i in range(len(pmf)))

# Calculate relative errors
mean_error = np.sqrt(variance / N) / mean
variance_error = np.sqrt(2 * variance ** 2 / N) / variance

# Calculate chi-squared statistic
expected_freqs = [N * pmf[i] for i in range(len(pmf))]
observed_freqs = [sum(1 for outcome in outcomes if outcome == i) for i in range(len(pmf))]
chi_squared, p_value = chisquare(observed_freqs, f_exp=expected_freqs)
chisquare()
# Plot bar chart of empirical probabilities
plt.bar(range(len(pmf)), empirical_probs)
plt.xticks(range(len(pmf)), range(1, len(pmf)+1))
plt.xlabel("Outcome")
plt.ylabel("Empirical Probability")
plt.title("Simulation Results")
plt.show()

print("Sample mean:", mean)
print("Sample variance:", variance)
print("Relative error of mean:", mean_error)
print("Relative error of variance:", variance_error)
print("Chi-squared statistic:", chi_squared)
print("p-value:", p_value)
