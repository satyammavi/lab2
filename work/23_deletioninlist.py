# Create a list of 20 numbers from user input
numbers = []

print("Enter 20 numbers:")
for i in range(20):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("\nOriginal List:", numbers)

# Ask user for number to delete
delete_num = int(input("\nEnter a number to delete (all occurrences except first): "))

# Check if number exists in list
if delete_num in numbers:
    first_index = numbers.index(delete_num)  # Find first occurrence
    
    # Remove all occurrences
    numbers = [x for x in numbers if x != delete_num]
    
    # Insert first occurrence back at original position
    numbers.insert(first_index, delete_num)

    print("\nUpdated List:", numbers)
else:
    print("\nNumber not found in the list.")