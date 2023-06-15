import random
import numpy
from math import floor

# probability = floor(random.random() * 100)

# initial number of trials
ini_number_of_trials = 0

# number of attempt that can be made
number_of_trials = int(input("Enter Number of times to Iterate: "))

print('Will it Rain? ')

while ini_number_of_trials < number_of_trials:
    probability = floor(random.random() * 100)
    print(probability)

    if probability >= 50:
        if (probability > 50) and (probability < 65):
            print(f'It will be rainy at probability of {probability} with slight wind ')

        elif (probability > 65) and (probability < 80):
            print(f'It will be an heavy rain at probability of {probability} with slight wind ')

        else:
            print(f'It will be an heavy rain at probability of {probability} with high speed of wind ')

    elif (probability < 50) and (probability > 1):
        # print("Yes,It will rain")
        # print("No, it won't be rainy today")

        if (probability > 35) and (probability < 50):
            print(f"it will be sunny at the probability of {probability} but will be slight windy")

        else:
            print(f"It will be sunny and the wind will be normal today, remember to have your sun-shades with you")

    ini_number_of_trials += 1


if ini_number_of_trials == number_of_trials:
    print('Reached, Exited- Try Again')
