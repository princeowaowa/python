def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

input_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(input_fahrenheit)
print(f"Temperature in Celsius: {celsius}")