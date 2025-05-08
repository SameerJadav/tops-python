# Practical Example 1: Write a Python program to print each fruit in a list using a simple for loop. List1 = ['apple', 'banana', 'mango']
list1 = ["apple", "banana", "mango"]
for fruit in list1:
    print(fruit, end=" ")
print()

# Practical Example 2: Write a Python program to find the length of each string in List1.
print(len(list1))

# Practical Example 3: Write a Python program to find a specific string in the list using a simple for loop and if condition.
mango = "mango"
for fruit in list1:
    if fruit == mango:
        print("found mango")
    else:
        print("could not find mango")

"""
Practical Example 4: Print this pattern using nested for loop:
*
**
***
****
*****
"""
for row in range(5):
    for col in range(row + 1):
        print("*", end="")
    print()
