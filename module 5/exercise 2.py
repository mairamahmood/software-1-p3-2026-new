numbers = []

while True:
    entry = input("Enter a number (or press Enter to quit): ")
    if entry == "":
        break
    numbers.append(int(entry))

# Sort descending and print top 5
numbers.sort(reverse=True)
top_five = numbers[:5]

print("The five greatest numbers are:")
for num in top_five:
    print(num)