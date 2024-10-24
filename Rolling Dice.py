# Rolling dice
# Roll the dice for the user
import random


user_input = (input("Roll the dice? (y/n) \n")).lower()
how_many_times = int(input("Enter, how many dice you want to roll? \n"))
count = 0
while count < how_many_times:
    if user_input == "y":
        roll_1 = random.randint(1, 6)
        roll_2 = random.randint(1, 6)
        print("Dice Results\n (%s,%s)" % (roll_1, roll_2))
        # The user input if he wants to roll again
        user_input = (input("Do you want to roll again? (y/n)\n")).lower()
        count = count + 1
    elif user_input == "n":
        print("Thanks for playing")
        break
    else:
        print("Invalid, Please Enter the correct option : ")
        user_input = (input("Roll the dice? (y/n)\n")).lower()
print("Reached the maximum roll, Thanks")
