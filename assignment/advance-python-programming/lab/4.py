# Write a Python program to read the contents of a file and print them on the console
with open("test.txt", "r") as file:
    print(file.read())

# Write a Python program to write multiple strings into a file
with open("test.txt", "w") as file:
    file.write("c\n")
    file.write("python\n")
    file.write("javascript\n")
