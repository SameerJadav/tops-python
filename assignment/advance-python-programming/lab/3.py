# Write a Python program to open a file in write mode, write some text, and then close it

# The file is automatically closed when using `with`
with open("test.txt", "w") as file:
    file.write("python\n")
