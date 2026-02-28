airports = {}

while True:
    print("\nOptions: 1=Enter new airport, 2=Fetch airport, 3=Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        code = input("Enter ICAO code: ").upper()
        name = input("Enter airport name: ")
        airports[code] = name
        print(f"{code} added.")

    elif choice == "2":
        code = input("Enter ICAO code to fetch: ").upper()
        if code in airports:
            print("Airport name:", airports[code])
        else:
            print("Airport not found")

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid option")