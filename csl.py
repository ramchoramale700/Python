import math

def calculator():
    print("\nSelect Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Logarithm (log base 10)")
    print("7. Exponent (x^y)")
    print("8. Square Root (√x)")
    print("9. Cube (x³)")
    print("10. Factorial (x!)")

    choice = input("Enter choice (1-10): ")

    if choice in ['1', '2', '3', '4', '5', '6', '7']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", num1 + num2)
        elif choice == '2':
            print("Result:", num1 - num2)
        elif choice == '3':
            print("Result:", num1 * num2)
        elif choice == '4':
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Division by zero!")
        elif choice == '5':
            print("Result:", num1 % num2)
        elif choice == '6':
            if num1 > 0:
                print("Result: log10(", num1, ") =", math.log10(num1))
        elif choice == '7':
            print("Result:", num1 ** num2)

    elif choice == '8':
        num = float(input("Enter number: "))
        if num >= 0:
            print("Result: √", num, "=", math.sqrt(num))

    elif choice == '9':
        num = float(input("Enter number: "))
        print("Result:", num, "³ =", num ** 3)
    elif choice == '10':
        num = int(input("Enter a non-negative integer: "))
        if num >= 0:
            print("Result: ", num, "! =", math.factorial(num))

    else:
        print("Invalid Input")

calculator()
