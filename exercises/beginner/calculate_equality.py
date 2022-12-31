# Create a function which determines is 3 numbers are equal and sum and multiply by 3 if they aren´t just sum

def sum_numbers(num1, num2, num3):
    sum_list = [num1, num2, num3]
    if num1 == num2 and num2 == num3:
        return sum(sum_list) * 3
    else:
        return sum(sum_list)

num1 = int(input('Please enter the first number: '))
num2 = int(input('Please enter the second number: '))
num3 = int(input('Please enter the third number: '))

print(sum_numbers(num1, num2, num3))