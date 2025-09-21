
# Pythonic features

nums = [1,2,3,4,5]
squares = [x*x for x in nums]  # List of squares

text = "hello world"
print(text[::-1])  # Reversed string

with open("data.txt") as f:
    for line in f:
        print(line.strip())  # Print each line without spaces