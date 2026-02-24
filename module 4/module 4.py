#Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.
number = 1

while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1

#Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
while True:
    inches = float(input("Enter inches (negative value to quit): "))

    if inches < 0:
        print("Program ended.")
        break

    centimeters = inches * 2.54
    print(f"{inches} inches is {centimeters} cm")

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
