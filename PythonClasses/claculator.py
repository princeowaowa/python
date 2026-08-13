class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9


calc = Calculator()

add1 = calc.add(5, 3)
print(f"Addition: {add1}")  # Output: Addition: 8   


celsius1 = calc.fahrenheit_to_celsius(68)
print(f"68°F in Celsius: {celsius1}")  # Output: 68°F in Celsius: 20.0