# Seasons tuple
seasons = ("Winter", "Spring", "Summer", "Autumn")

month = int(input("Enter month number (1-12): "))

if month in [12, 1, 2]:
    print("Season:", seasons[0])  # Winter
elif month in [3, 4, 5]:
    print("Season:", seasons[1])  # Spring
elif month in [6, 7, 8]:
    print("Season:", seasons[2])  # Summer
elif month in [9, 10, 11]:
    print("Season:", seasons[3])  # Autumn
else:
    print("Invalid month number")