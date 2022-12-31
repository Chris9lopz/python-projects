# Create a funcion which determines if the given number is nearest to 1000 or 2000

def nearest_number(number):
    """Determines if the given number is nearest to 1000 or 2000"""
    if abs(1000 - number) < 100 or abs(2000 - number) < 100:
        return True
    else:
        return False

user_input = int(input('Please enter a number: '))

print(nearest_number(user_input))
