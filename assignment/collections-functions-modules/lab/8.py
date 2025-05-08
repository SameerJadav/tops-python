# Write a Python program to create a function that takes a string as input and prints it.
def echo(str: str):
    print(str)


echo(input("enter a string: "))

# Write a Python program to create a calculator using functions


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "Error! Division by zero is not allowed."
    return num1 / num2


def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        try:
            choice = input("Enter choice(1/2/3/4): ")

            if choice in ("1", "2", "3", "4"):
                num1_str = input("Enter first number: ")
                num2_str = input("Enter second number: ")
                num1 = float(num1_str)
                num2 = float(num2_str)

                if choice == "1":
                    print(num1, "+", num2, "=", add(num1, num2))
                elif choice == "2":
                    print(num1, "-", num2, "=", subtract(num1, num2))
                elif choice == "3":
                    print(num1, "*", num2, "=", multiply(num1, num2))
                elif choice == "4":
                    print(num1, "/", num2, "=", divide(num1, num2))
                break
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")


calculator()
