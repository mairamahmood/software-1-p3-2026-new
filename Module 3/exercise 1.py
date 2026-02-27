length = int(input("Enter the length of the zander in centimeters: "))

size_limit = 42

if length < size_limit:
    difference = size_limit - length
    print("The zander is too small.")
    print(f"Release the fish back into the lake.")
    print(f"It is {difference} cm below the size limit.")
else:
    print("The zander meets the size limit. You may keep it.")
-