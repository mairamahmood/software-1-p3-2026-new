#Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
while True:
    inches = float(input("Enter inches (negative value to quit): "))

    if inches < 0:
        print("Program ended.")
        break

    centimeters = inches * 2.54
    print(f"{inches} inches is {centimeters} cm")