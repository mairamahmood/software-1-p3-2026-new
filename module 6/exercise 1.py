import random

def roll_dice():
    """Return a random dice roll between 1 and 6."""
    return random.randint(1, 6)

# Main program: roll until 6
while True:
    result = roll_dice()
    print("Rolled:", result)
    if result == 6:
        break