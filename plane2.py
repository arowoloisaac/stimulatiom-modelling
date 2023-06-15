import numpy as np
import matplotlib.pyplot as plt
import time

# start time
st = time.time()

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
rho = 1.2  # Air density (kg/m^3)
Cd = 0.5  # Drag coefficient
A = 0.01  # Cross-sectional area (m^2)
m = 0.2  # Mass of rocket (kg)
v0 = 100  # Initial velocity (m/s)
theta = np.pi / 4  # Launch angle (radians)


# Time interval and step size
t_start = 0
t_end = 20
dt = 0.5
t = np.arange(t_start, t_end, dt)

# Arrays for storing values
x = np.zeros(len(t))
y = np.zeros(len(t))
vx = np.zeros(len(t))
vy = np.zeros(len(t))

# Initial conditions
x[0] = 0
y[0] = 0
vx[0] = v0 * np.cos(theta)
vy[0] = v0 * np.sin(theta)
time.sleep(3)

# Numerical integration using Euler's method
for i in range(1, len(t)):
    # Calculate air resistance
    v = np.sqrt(vx[i - 1] ** 2 + vy[i - 1] ** 2)
    Fd = -0.5 * rho * Cd * A * v ** 2
    ax = Fd / m * np.cos(theta)
    ay = -g + Fd / m * np.sin(theta)

    # Update velocities and positions
    vx[i] = vx[i - 1] + ax * dt
    vy[i] = vy[i - 1] + ay * dt
    x[i] = x[i - 1] + vx[i] * dt
    y[i] = y[i - 1] + vy[i] * dt

    # If the rocket hits the ground, stop simulation
    if y[i] < 0:
        break

# Plot the trajectory
plt.plot(x[:i], y[:i])

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st

plt.xlabel('Horizontal distance (m)')
plt.ylabel('Height (m)')
plt.title('Flight in Atmosphere')
plt.grid()
plt.show()

# et = time.time()
#
# # get the execution time
# elapsed_time = et - st


print('dt', dt)
print('Execution time:', elapsed_time, 'seconds')


# In this example, we first define some constants like the acceleration due to gravity, the density of air
# at sea level, the drag coefficient, the cross-sectional area of the object, and the mass of the object.
# We also define the initial conditions for the simulation, including the initial velocity and height.

# Next, we set some simulation parameters like the time step and the maximum simulation time.
# We create three arrays to store the simulation results, one for time, one for height, and one for velocity.

# We then simulate the flight by iterating over the time array and updating the velocity and height based
# on the forces acting on the object. We use the break statement to stop the simulation if the object hits
# the ground.

