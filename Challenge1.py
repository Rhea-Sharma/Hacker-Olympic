# Imports the method 'randint' from the library 'random'
from random import randint

# Prompts the user to choose the range of possible numbers
lower_bound = int(input("Enter an integer for the lower bound: "))
upper_bound = int(input("Enter an integer for the upper bound: "))

if lower_bound > upper_bound:
    print("Error. Make sure the upper bound is larger than the lower bound.")
    lower_bound = int(input("Enter an integer for the lower bound: "))

# Generates a random number based on the given range
rand_num = randint(lower_bound, upper_bound)

# Prompts the user to guess a number in the range
num = int(input("Make a guess between {} and {}: ".format(lower_bound, upper_bound)))

if not isinstance(num, int):
    print("Error.Only integers are allowed")
    num = int(input("Please enter another integer: "))

while num < lower_bound or num > upper_bound:
    print("This number is not in range. Please guess a number between {} and {}. ".format(lower_bound, upper_bound))
    num = int(input("Enter a number: "))

while num >= lower_bound and num <= upper_bound:

    if num > rand_num:
        print("Incorrect. The number is lower.")
        num = int(input("Please enter another integer: "))

    if num < rand_num:
        print("Incorrect. The number is higher.")
        num = int(input("Please enter another integer: "))

    if num == rand_num:
        print("Congratulations! You guessed the number!")
        break
