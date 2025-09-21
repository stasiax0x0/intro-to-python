
# Programming paradigms

# Procedural: function to calculate factorial
def factorial(n):
        result = 1
        for i in range(1, n+1):
                result *= i
        return result

# OOP: Dog class with bark method
class Dog:
        def __init__(self, name):
                self.name = name
        def bark(self):
                print(f"{self.name} says woof!")

# Functional: create a list of squares
nums = [1, 2, 3, 4, 5]
squares = [x*x for x in nums]