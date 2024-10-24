# Number Guessing Game
import random

min_value_from_the_user = int(input("Enter the minimum value: \n"))
max_value_from_the_user = int(input("Enter the maximum value: \n"))
print("You have 4 attempts! Good luck")
user_input_number = int(
    input(
        "Guess the number between\n (%s - %s)\n"
        % (min_value_from_the_user, max_value_from_the_user)
    )
)

attempts = 4
random_number = random.randint(min_value_from_the_user, max_value_from_the_user)
counts = 1
while counts <= attempts:
    if user_input_number < random_number:
        user_input_number = int(input("Too low! Try again\n"))
    elif user_input_number > random_number:
        user_input_number = int(input("Too high! Try again\n"))
    else:
        print("Best score so far\n")
        print("Congratulations! You guessed the number in %s" % counts, " attempts")
        break
    counts = counts + 1
else:
    print("You have reached the maximum attempt\n The number was : ", random_number)
