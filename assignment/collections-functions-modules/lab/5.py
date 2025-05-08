# Write a Python program to access values between index 1 and 5 in a tuple
nums = (1, 2, 3, 4, 5)

for num in nums:
    print(num)

# Write a Python program to access alternate values between index 1 and 5 in a tuple
for num in nums:
    if num % 2 == 1:
        print(num)
