import random
import statistics

def simulate_events(events, probs, time_step, end_time):
    time = 0
    stats = [0] * len(events)
    while time < end_time:
        r = random.random()
        p = 0
        for i, event in enumerate(events):
            p += probs[i]
            if r < p:
                stats[i] += 1
                break
        time += time_step
    return stats


def gather_statistics(num_simulations, events, probs, time_step, end_time):
    counts = []
    for i in range(num_simulations):
        stats = simulate_events(events, probs, time_step, end_time)
        counts.append(stats)
    mean_counts = [statistics.mean(c) for c in zip(*counts)]
    std_dev_counts = [statistics.stdev(c) for c in zip(*counts)]
    return mean_counts, std_dev_counts


# events = ['event1', 'event2', 'event3']
# probs = [] # 0.2, 0.3, 0.5
# for i in range(3):
#     ran = random.random()
#     probs.append(ran)
#
# print(probs)
# events = []
n = int(input('Number of recursion: '))
events = [event+1 for event in range(n+1)]

probs = []

prob_sum = 0

for i in range(n):
    inp_prob = float(input(f'input the number {i+1} float: '))
    probs.append(inp_prob)

    prob_sum = sum(probs)

if prob_sum < 1:
   check_sum = 1 - prob_sum
   probs.append(round(check_sum, 3))

elif prob_sum == 1 or prob_sum > 1:
    probs.append(0.01)

else:
    print('not equal')

# print(f"{prob_sum: .2f}")
# print(check_sum)
# print(probs)

time_step = 1
end_time = 10

# check = []
mean_counts = 0

num_simulations_list = [100]
for num_simulations in num_simulations_list:
    print(f'Number of simulations: {num_simulations}')
    print(probs)
    mean_counts, std_dev_counts = gather_statistics(num_simulations, events, probs, time_step, end_time)
    print('Event\tMean\tStd Dev\tProbability')
    for event, mean, std_dev, prob in zip(events, mean_counts, std_dev_counts, probs):
        print(f'{event}\t\t{mean:.2f}\t\t{std_dev:.2f}\t\t{prob:.2f}')
    print('------------------')
    # check.append(mean_counts)

# print(check)
print(mean_counts)

import matplotlib.pyplot as plt

# events = ['event1', 'event2', 'event3']
# probs = [0.2, 0.3, 0.5]

plt.bar(events, probs) # probs mean_counts
plt.title('Event Probabilities')
plt.xlabel('Event')
plt.ylabel('Probability')
# plt.ylim([0, 1])
plt.show()
