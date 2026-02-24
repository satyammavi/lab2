num = int(input("Enter the number:"))
# Check if the number is even or odd without using the modulus operator
if num // 2 * 2 == num:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")
