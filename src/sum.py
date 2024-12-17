import os

num1 = int(os.getenv('NUMBER_1', 0))
num2 = int(os.getenv('NUMBER_2', 0))

result = num1 + num2

print(f"the sum of {num1} and {num2} is {result}")
