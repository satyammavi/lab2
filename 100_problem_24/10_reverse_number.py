number = int(input("Enter a number to reverse: "))
original_number = number
reverse_number = 0

while number > 0:
    reverse_number = reverse_number * 10 + number % 10
    number //= 10
print(f"The reverse of {original_number} is {reverse_number}")
