import random
print("Welcome to this dice rolling simulator!")
roll = input("Press ENTER to roll and 'q' to quit. ")
while roll.lower() != "q":
    number = random.randint(1, 6)
    print("You rolled a %d." % number)
    roll = input("Press ENTER to roll again and 'q' to quit.")
    if roll.lower == "q":
        break
if roll == 'q'.lower():
    print("Thanks for playing!")
