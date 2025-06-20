# Swap keys and values in a dictionary in Python

"""
Your task for today is to write a Python program that swaps
the keys and values in a dictionary. That means turning something
like {'a': 1, 'b': 2} into {1: 'a', 2: 'b'}.
"""
# Solution
dictionary = {'a': 1, 'b': 2, 'c': 3}
reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
print(reverse_dictionary)
