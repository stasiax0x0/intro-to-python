
# Standard library

import random, json  # Import random and json modules
print(random.randint(1,6))  # Random number between 1 and 6

student = {"name": "Alice", "year": 2}
data = json.dumps(student)  # Convert dictionary to JSON string
print(data)