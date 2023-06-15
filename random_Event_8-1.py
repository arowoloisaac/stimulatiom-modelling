import random
import numpy
from math import floor

guess_number = floor(random.random() * 5) + 1

# probability = floor(random.random() * 100)


# print(probability)

print(guess_number)

# initial number of trials
ini_number_of_trials = 0

# number of attempt that can be made
number_of_trials = 3

check = print('Check whether rainy or Not ')

while ini_number_of_trials < number_of_trials:
    probability = floor(random.random() * 100)
    print(probability)

    if probability >= 90:
        # print("Yes,It will rain")
        print("No, it won't be rainy today")

    elif probability < 90 and probability > 1:
        print("Yes,It will rain")
        # print("No, it won't be rainy today")

    # inputted number to be guessed


    ini_number_of_trials += 1


if ini_number_of_trials == number_of_trials:
    print('Reached, Exited- Try Again')
