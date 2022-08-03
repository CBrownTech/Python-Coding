import random
import math
lower = int(input("Enter the lowest number: "))
upper = int(input("Enter the highest number: "))
# Generating a random number between lower and upper bound.
x = random.randint(lower, upper)
print("\n\tYou have only ", round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")
# Initializing the number of guesses.
count = 0
# This is for the calculation of the minimum number of guesses, depending on the range.
while count < math.log(upper - lower + 1, 2):
    count += 1
    # Taking the guessing number as the input
    guess = int(input("Guess a number: "))
    # Condition testing
    if x == guess:
        print("Congratulations! The number of tries you guessed it was: ",count)
        break
    elif x > guess:
        print("You guessed too low!")
    elif x < guess:
        print("You guessed too high!")
if count >= math.log(upper - lower + 1, 2):
    print("\nSorry. The number is %d." % x)
    print("\tBetter luck next time!")
