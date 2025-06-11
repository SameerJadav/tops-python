import re

text = "The quick brown fox jumps over the lazy dog."
pattern = "fox"

# Write a Python program to search for a word in a string using re.search()
match = re.search(pattern, text)

# Write a Python program to match a word in a string using re.match()
if match:
    print("word found:", match.group())
else:
    print("word not found")
