names_set = set()

while True:
    name = input("Enter a name (empty to quit): ")

    if name == "":
        break

    if name in names_set:
        print("Existing name")
    else:
        print("New name")
        names_set.add(name)

print("\nAll names entered:")
for n in names_set:
    print(n)