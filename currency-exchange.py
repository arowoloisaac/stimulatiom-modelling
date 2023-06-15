import numpy as np
import matplotlib.pyplot as plt
import time


st = time.time()

# Parameters
n = 50  # Number of time steps
mu1 = 0.05  # Mean return rate for currency 1
sigma1 = 0.1  # Volatility for currency 1 --- 0.1
mu2 = 0.03  # Mean return rate for currency 2
sigma2 = 0.3  # Volatility for currency 2 --- 0.07
rho = 0.3  # Correlation between currency 1 and currency 2 --- -0.5
S1_0 = 3  # Initial exchange rate for currency 1
S2_0 = 5  # Initial exchange rate for currency 2

# Generate random returns
dt = 1 / 10  # Time step  252
cov_matrix = np.array([[sigma1 ** 2, rho * sigma1 * sigma2],
                       [rho * sigma1 * sigma2, sigma2 ** 2]])
rand_matrix = np.random.multivariate_normal(mean=[mu1, mu2], cov=cov_matrix, size=n)
rand_returns = np.exp(rand_matrix * np.sqrt(dt))

# Calculate exchange rates
S1 = S1_0 * np.cumprod(rand_returns[:, 0])
S2 = S2_0 * np.cumprod(rand_returns[:, 1])

et = time.time()

# get the execution time
elapsed_time = et - st

time.sleep(5)
# Plot results
fig, ax = plt.subplots()
ax.plot(S1, label='Currency 1', color='yellow')
ax.plot(S2, label='Currency 2', color='blue')
ax.legend()

ax.set_xlabel('Time')
ax.set_ylabel('Exchange rate')
plt.show()

print(rand_returns)


# First, we set some parameters, including the number of time steps n, the mean return rate and volatility
# for each currency (mu1, sigma1, mu2, sigma2), the correlation between the two currencies (rho), and the
# initial exchange rates for each currency (S1_0, S2_0).

# Next, we generate random returns for each currency using a multivariate normal distribution with the given
# means, volatilities, and correlation.

