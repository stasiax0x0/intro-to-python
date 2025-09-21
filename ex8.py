#functions

def greet(name="World"):
    return f"Hello, {name}"

def stats(nums):
    return min(nums), max(nums), sum(nums)/len(nums)

print(greet("Alice"))
print(stats([3, 5, 9]))
