#exercise 4
cities = []

# Read 5 city names
for i in range(5):
    city = input(f"Enter the name of city {i+1}: ")
    cities.append(city)

# Print cities
print("The cities you entered are:")
for city in cities:
    print(city)