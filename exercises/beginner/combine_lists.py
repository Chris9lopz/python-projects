"""
Create a function combine_lists that:

Takes two lists of numbers of identical size (ls1 and ls2).
Returns a new list of numbers.
Each number in the returned list must be the sum
of corresponding elements of lists ls1 and ls2, like so:

result_list[i] = ls1[i] + ls2[i]

For example:

combine_lists([1, 2, 5], [3, 6, 1])  # [4, 8, 6].
combine_lists([1], [6])  # [7].
combine_lists([], [])  # [].
"""


def combine_lists(ls1, ls2):

    new_list = [ls1[i] + ls2[i] for i in range(len(ls1))]

    return new_list
