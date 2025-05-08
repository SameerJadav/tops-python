# Practical Example 5: Write a Python program to find greater and less than a number using if_else.
num1 = 10
num2 = 20
if num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")

# Practical Example 6: Write a Python program to check if a number is prime using if_else.
num = int(input("enter a number: "))
count = 0
for i in range(2, num - 1):
    if num % i == 0:
        count += 1
if count == 0:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

# Practical Example 7: Write a Python program to calculate grades based on percentage using if-else ladder.
marks = int(input("enter marks: "))
if marks >= 70:
    print("A grade")
elif marks >= 60:
    print("B grade")
elif marks >= 50:
    print("C grade")
else:
    print("Fail")

# Practical Example 8: Write a Python program to check if a person is eligible to donate blood using a nested if.
age = int(input("enter your age: "))
if age >= 18:
    print("you are eligible ot donate blood")
else:
    print("you are eligible ot donate blood")
