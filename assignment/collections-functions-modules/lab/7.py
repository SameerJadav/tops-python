# Write a Python program to update a value in a dictionary
student = {
    "name": "sameer",
    "age": 21,
    "email": "sameer@gmail.com",
    "course": "backend",
    "language": "python",
    "center": "CG",
}

print(student)
student["course"] = "frontend"
print(student)

# Write a Python program to merge two lists into one dictionary using a loop
keys_list = ["name", "age", "course"]
values_list = ["sameer", 21, "backend"]
merged_dict = {}
for i in range(len(keys_list)):
    merged_dict[keys_list[i]] = values_list[i]
print(merged_dict)
