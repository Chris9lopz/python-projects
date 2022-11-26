# Convert numbers followed by comma in a list

def numbers_to_string(numbers):
    list_add = [] # Create a empty list
    for i in range(0,len(numbers),2): 
        list_add.append(int(numbers[i]))
    print(list_add)


user_input = input('Enter numbers followed by comma without space: ')

numbers_to_string(user_input)

# Other way to solve could be using .split() method