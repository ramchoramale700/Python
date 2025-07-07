import math

def addition(a, b):
    print("Result:", a + b)

def subtraction(a, b):
    print("Result:", a - b)

def multiplication(a, b):
    print("Result:", a * b)

def division(a, b):
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero!")

def modulus(a, b):
    print("Result:", a % b)

def logarithm(a):
    if a > 0:
        print("Result: log10(", a, ") =", math.log10(a))
    else:
        print("Error: Logarithm undefined for non-positive values")

def exponent(a, b):
    print("Result:", a ** b)

def square_root(n):
    if n >= 0:
        print("Result: √", n, "=", math.sqrt(n))
    else:
        print("Error: Cannot take square root of a negative number")

def cube(n):
    print("Result:", n, "³ =", n ** 3)

def factorial(n):
    if n >= 0:
        print("Result:", n, "! =", math.factorial(n))
    else:
        print("Error: Factorial is not defined for negative numbers")

def calculator():
    print("Welcome to simple calculator")
    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Logarithm")
    print("7. Exponent")
    print("8. Square Root")
    print("9. Cube")
    print("10. Factorial")

    choice = input("Enter choice (1-10): ")

    if choice in ['1', '2', '3', '4', '5', '7']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            addition(num1, num2)
        elif choice == '2':
            subtraction(num1, num2)
        elif choice == '3':
            multiplication(num1, num2)
        elif choice == '4':
            division(num1, num2)
        elif choice == '5':
            modulus(num1, num2)
        elif choice == '7':
            exponent(num1, num2)

        elif choice == '6':
            num = float(input("Enter number: "))
            logarithm(num)

        elif choice == '8':
            num = float(input("Enter number: "))
            square_root(num)

        elif choice == '9':
            num = float(input("Enter number: "))
            cube(num)

        elif choice == '10':
            num = int(input("Enter a non-negative integer: "))
            factorial(num)

        else:
            print("Invalid choice.")

calculator()
