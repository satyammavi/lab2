digit = int(input("Enter the number:"))
sum_of_digits = 0

while digit > 0:
    sum_of_digits += digit % 10
    digit //= 10
print(f"The sum of the digits is {sum_of_digits}")
