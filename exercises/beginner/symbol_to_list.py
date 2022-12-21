# Exercise get a of numbers separated by comma and create a new list

user_number = input('Please enter numbers followed by comma: ')


def comma_into_list(user_input):

    return user_input.split(',')


result = comma_into_list(user_number)

print(result)
