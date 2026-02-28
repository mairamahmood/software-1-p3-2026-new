def remove_odd_numbers(numbers):
    """Return a new list with all odd numbers removed."""
    return [num for num in numbers if num % 2 == 0]

# Main program
original_list = [1, 2, 3, 4, 5, 6, 7]
filtered_list = remove_odd_numbers(original_list)

print("Original list:", original_list)
print("List without odd numbers:", filtered_list)