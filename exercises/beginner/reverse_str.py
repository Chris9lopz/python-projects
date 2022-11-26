# Exercise reverse a string 

def reverse_string(word):
    result = word[::-1]
    return result

word_input = input('Please enter the string to reverse: ')

print(reverse_string(word_input))
