import numpy as np
import matplotlib.pyplot as plt
import time

# Define the possible states
states = ["clear", "windy", "overcast"]

# Define the transition rate matrix
transition_rates = np.array([[0.7, 0.2, 0.1], [0.4, 0.3, 0.3], [0.1, 0.5, 0.4]])

# Set the initial state to "clear"
current_state = "clear"

# Set the simulation duration to 30 days
sim_duration = 10

# Initialize lists to store the weather state and time data
weather_states = [current_state]
time_data = [0]

# Start the timer
start_time = time.time()

# Simulate the weather for the specified duration
for day in range(1, sim_duration + 1):
    # Determine the probabilities of transitioning to each state
    probabilities = transition_rates[states.index(current_state), :]
    # Randomly select the next state based on the probabilities
    next_state = np.random.choice(states, p=probabilities)
    # Update the current state to the next state
    current_state = next_state
    # Append the current state and timedata to the lists
    weather_states.append(current_state)
    time_data.append(day)

    # Print the current and next states
    print(f"On day {day}, the weather is {current_state} and will transition to {next_state}")

    # Plot the weather state changes
    plt.clf()
    plt.plot(time_data, [states.index(state) for state in weather_states])
    plt.xticks(time_data, time_data)
    plt.xlabel('Time (days)')
    plt.ylabel('Weather State')
    plt.title('Weather Simulation')
    plt.draw()
    plt.pause(0.5)

# Stop the timer and calculate the simulation time
end_time = time.time()
sim_time = end_time - start_time



# Print the simulation time
print(f"Simulation complete in {sim_time:.2f} seconds")

# Calculate the frequency of each weather state
freq_clear = weather_states.count("clear") / len(weather_states)
freq_windy = weather_states.count("windy") / len(weather_states)
freq_overcast = weather_states.count("overcast") / len(weather_states)

# Print the frequency of each weather state
print(f"Frequency of clear weather: {freq_clear:.2f}")
print(f"Frequency of windy weather: {freq_windy:.2f}")
print(f"Frequency of overcast weather: {freq_overcast:.2f}")

# Calculate the stationary distribution of the weather states
stationary_dist = np.linalg.eig(transition_rates.T)[1][:, 0]
stationary_dist = stationary_dist / np.sum(stationary_dist)

# Print the stationary distribution of the weather states
print(f"Stationary distribution of weather states: {stationary_dist}")
