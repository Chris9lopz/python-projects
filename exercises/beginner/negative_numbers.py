# Filter Negative Numbers from a List in Python
"""
Project Description
Your task for today is to write a Python program that takes a list of
numbers and removes all the negative ones. The goal is to keep only numbers
that are greater than or equal to zero.
"""

numbers = [3, -1, 7, -5, 0, 8, -2]

positive_numbers = [i for i in numbers if i >= 0]

print(positive_numbers)
