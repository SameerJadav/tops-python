# Write a Python program to create a class and access its properties using an object
class Student:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(self.name)


student = Student("Sameer")
student.display_name()
