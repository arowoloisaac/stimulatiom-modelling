import numpy as np
import matplotlib.pyplot as plt

# Define the state space and transition rate matrix
states = ["clear", "windy", "overcast"]
transition_rates = np.array([[-0.4, 0.2, 0.1],
                            [0.3, -0.5, 0.2],
                            [-0.2, 0.3, 0.5]])

# Define the initial state and simulation duration
state_0 = 'clear'
total_time = 10  # Total simulation time (in arbitrary units)

# Normalize the transition rate matrix to obtain transition probabilities
transition_probs = np.exp(transition_rates * total_time)
transition_probs /= np.sum(transition_probs, axis=1, keepdims=True)

# Initialize the state and time
state = state_0
time = 0

# Lists to store the simulated state and time
simulated_state = [state]
simulated_time = [time]

# Simulate the Markov process
while time < total_time:
    # Generate a random number for the time until the next transition
    dt = np.random.exponential(scale=1 / np.abs(transition_rates[states.index(state), states.index(state)]))

    # Update the time and state
    time += dt
    print(f"On day {time}, the weather is {state}")
    next_state = np.random.choice(states, p=transition_probs[states.index(state)])
    state = next_state

    # Store the simulated state and time
    simulated_state.append(state)
    simulated_time.append(time)

    print(f"transition to {next_state}")

# Plot the simulated Markov process
plt.step(simulated_time, simulated_state)
plt.xlabel('Time')
plt.ylabel('State')
plt.xticks(np.arange(0, total_time + 1, 1))
plt.yticks(range(len(states)), states)
plt.show()

# Calculate statistical processing
state_counts = np.bincount([states.index(s) for s in simulated_state])
state_probabilities = state_counts / len(simulated_state)
print("State Probabilities:", state_probabilities)

# Calculate stationary distribution
stationary_dist = np.linalg.eig(transition_rates.T)[1][:, 0]
stationary_dist /= np.sum(stationary_dist)
print("Stationary Distribution:", stationary_dist)

