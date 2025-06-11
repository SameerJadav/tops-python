# Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).
# Write a Python program to demonstrate handling multiple exceptions


def divide(numerator, denominator):
    try:
        result = numerator / denominator
        print(f"{numerator}/{denominator} = {result}")
    except ZeroDivisionError:
        print("cannot divide by zero")
    except TypeError:
        print("both numerator and denominator must be numbers")
    except Exception as e:
        print(f"an unexpected error occurred: {e}")


divide(10, 2)
divide(5, 0)
divide("10", 2)
divide(8, "four")
divide([1, 2], 3)
