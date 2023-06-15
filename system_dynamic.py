import matplotlib.pyplot as plt
import random

# Initial state variables
revenue = 0
guests = 0
capacity = 50
satisfaction = 0.8
price = 15
quality = 0.8
demand = 0.2

# Simulation parameters
num_hours = 24
time_step = 1

# Lists to store the state variables at each time step
revenue_list = [revenue]
guests_list = [guests]
capacity_list = [capacity]
satisfaction_list = [satisfaction]

# Simulation loop
for hour in range(num_hours):
    # Calculate the number of guests for this hour
    num_guests = int(capacity * demand * satisfaction)

    # Update the number of guests and revenue
    guests += num_guests
    revenue += num_guests * price

    # Update the capacity based on the number of guests leaving
    capacity -= guests

    # Update the satisfaction level based on the quality of food and service
    satisfaction = max(min(satisfaction + random.uniform(-0.05, 0.05), 1), 0)
    quality = max(min(quality + random.uniform(-0.05, 0.05), 1), 0)
    satisfaction = satisfaction + 0.2 * (quality - satisfaction)

    # Update the demand based on the current satisfaction level
    demand = max(min(demand + random.uniform(-0.05, 0.05), 1), 0)
    demand = demand + 0.1 * (satisfaction - demand)

    # Update the price based on the current revenue and number of guests
    if guests == 0:
        price = price
    else:
        price = max(min(price + random.uniform(-1, 1), 30), 5)
        if revenue / guests < price:
            price = price - 1
        elif revenue / guests > price:
            price = price + 1

    # Append the current state variables to the lists
    revenue_list.append(revenue)
    guests_list.append(guests)
    capacity_list.append(capacity)
    satisfaction_list.append(satisfaction)

# Plot the trajectories of the state variables
fig, axs = plt.subplots(2, 2, figsize=(10, 12))
axs[0, 0].plot(range(num_hours + 1), revenue_list)
axs[0, 0].set_title("Revenue")
axs[0, 1].plot(range(num_hours + 1), guests_list)
axs[0, 1].set_title("Guests")
axs[1, 0].plot(range(num_hours + 1), capacity_list)
axs[1, 0].set_title("Capacity")
axs[1, 1].plot(range(num_hours + 1), satisfaction_list)
axs[1, 1].set_title("Satisfaction")

plt.tight_layout()
plt.show()
