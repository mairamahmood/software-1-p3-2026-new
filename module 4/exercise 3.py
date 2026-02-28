#Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program prints out the smallest and largest number from the numbers it received.
smallest = None
largest = None

while True:
    user_input = input("Enter a number (empty string to quit): ")

    if user_input == "":
        break

    number = float(user_input)

    if smallest is None or number < smallest:
        smallest = number

    if largest is None or number > largest:
        largest = number

if smallest is not None:
    print("Smallest number:", smallest)
    print("Largest number:", largest)
else:
    print("No numbers were entered.")
