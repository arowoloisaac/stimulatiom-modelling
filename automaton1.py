# import numpy as np
# import matplotlib.pyplot as plt
#
# # Set up the initial state of the automaton
# size = 100  # Size of the grid
# steps = 100  # Number of time steps to run
# grid = np.zeros((size, size), dtype=int)  # Initialize the grid with zeros
# grid[size//2, size//2] = 1  # Set the center cell to 1
#
#
# def transition_function(state):
#     # Create a copy of the current state to modify
#     new_state = np.copy(state)
#     # Iterate over all cells and apply the transition rule
#     for i in range(1, state.shape[0]-1):
#         for j in range(1, state.shape[1]-1):
#             # Count the number of neighbors that are "on"
#             neighbors = np.sum(state[i-1:i+2, j-1:j+2]) - state[i, j]
#             # Apply the transition rule
#             if state[i, j] == 1:
#                 if neighbors < 2 or neighbors > 3:
#                     new_state[i, j] = 0
#             else:
#                 if neighbors == 3:
#                     new_state[i, j] = 1
#     return new_state
#
#
# for t in range(steps):
#     grid = transition_function(grid)
#
# # Plot the final state of the automaton
# plt.imshow(grid, cmap='binary')
# plt.show()


# import cellpylib as cpl
#
# # Glider
# cellular_automaton = cpl.init_simple2d(60, 60)
# cellular_automaton[:, [28,29,30,30], [30,31,29,31]] = 1
#
# # Blinker
# cellular_automaton[:, [40,40,40], [15,16,17]] = 1
#
# # Light Weight Space Ship (LWSS)
# cellular_automaton[:, [18, 18, 19, 20, 21, 21, 21, 21, 20], [45,48,44,44,44,45,46,47,48]] = 1
#
# # evolve the cellular automaton for 60 time steps
# cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=60, neighbourhood='Moore',
#                                   apply_rule=cpl.game_of_life_rule, memoize="recursive")
#
# cpl.plot2d_animate(cellular_automaton)


import cellpylib as cpl

sdsr_loop = cpl.SDSRLoop()

# the initial conditions consist of a single loop
cellular_automaton = sdsr_loop.init_loops(1, (100, 100), [40], [40])

cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=700,
                                  apply_rule=sdsr_loop, memoize="recursive")

cpl.plot2d_animate(cellular_automaton)