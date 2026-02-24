fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
if fahrenheit < -459.67:
    print("Temperature cannot be below absolute zero.")
    exit()
# Calculating the temperature
calcius = (fahrenheit - 32) * 5 / 9
print(f"The temperature in Celsius is {calcius}")
