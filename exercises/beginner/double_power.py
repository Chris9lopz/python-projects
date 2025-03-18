"""
Double Power


Since the labels are ready, we'll know double the output of our robot factory.
Create a double_power function that:

Takes a list of current_powers.
Returns a list of doubled values.
⚠️ If the list is empty, return an empty list as well.

For example:

double_power([100, 150, 200, 220])  # [200, 300, 400, 440]
double_power([45, 34, 56, 67])  # [90, 68, 112, 134]
double_power([])  # []

"""


def double_power(current_powers):
    return [current_power * 2 for current_power in current_powers]
