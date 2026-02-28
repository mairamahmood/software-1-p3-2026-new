import random

# Ask user how many dice to roll
num_dice = int(input("How many dice do you want to roll? "))

total = 0
for _ in range(num_dice):
    roll = random.randint(1, 6)  # Roll a die (1-6)
    total += roll

print("The sum of the dice is:", total)