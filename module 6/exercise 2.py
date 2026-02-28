import random

def roll_dice(sides):
    """Return a random dice roll between 1 and 'sides'."""
    return random.randint(1, sides)

# Main program
max_side = int(input("Enter the number of sides on the dice: "))

while True:
    result = roll_dice(max_side)
    print("Rolled:", result)
    if result == max_side:
        break