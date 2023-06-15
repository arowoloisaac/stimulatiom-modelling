import numpy as np
import matplotlib.pyplot as plt

def simulate_exchange_rate(initial_rate, drift, volatility, time, num_steps):
    dt = time / num_steps
    t = np.linspace(0, time, num_steps)
    rates = np.zeros(num_steps)
    rates[0] = initial_rate

    for i in range(1, num_steps):
        drift_component = drift * t[i]
        variance_component = np.exp(2 * drift * t[i]) * (np.exp(volatility ** 2 * t[i]) - 1)
        randomness = np.random.normal(0, 1)
        rates[i] = rates[i - 1] * np.exp(drift_component + np.sqrt(variance_component) * randomness)

    return t, rates

# Parameters
initial_rate = 1.0    # Initial exchange rate
drift = 0.05         # Drift (expected return) of the exchange rate
volatility = 0.2     # Volatility (standard deviation of returns) of the exchange rate
time = 1.0           # Total time period (in years)
num_steps = 10      # Number of time steps (assuming daily data for a year)

# Simulate exchange rates
t1, rates1 = simulate_exchange_rate(initial_rate, drift, volatility, time, num_steps)
t2, rates2 = simulate_exchange_rate(initial_rate, drift, volatility, time, num_steps)

# Plot the simulated exchange rates
plt.plot(t1, rates1, label='Exchange Rate 1')
plt.plot(t2, rates2, label='Exchange Rate 2')
plt.xlabel('Time')
plt.ylabel('Exchange Rate')
plt.title('Simulated Currency Exchange Rates')
plt.legend()
plt.show()
