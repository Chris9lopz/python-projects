"""
Get Speed Statistic

The first batch of robots is ready, now they need to be tested.
All robots are unique, and each has its own speed. We need to find
the robots' lowest, highest, and average speed.

Create the get_speed_statistic function that:

Takes the test_results list of robots' speeds.
Returns statistics as a list with 3 numbers:
First — the lowest speed.
Second — the highest speed.
Third — the average speed, rounded down with from math import floor.

💡 If the test_results list is empty, return [0, 0, 0].

Example:

get_speed_statistic([])  # [0, 0, 0]
get_speed_statistic([10])  # [10, 10, 10]
get_speed_statistic([8, 9, 3, 12])  # [3, 12, 8]
get_speed_statistic([10, 10, 11, 9, 12, 8])  # [8, 12, 10]

"""

from math import floor


def average_production(robots_production: list) -> int:
    return floor(sum(robots_production) / len(robots_production))


def get_speed_statistic(test_results: list) -> list:
    if not test_results:
        return [0, 0, 0]
    return [min(test_results), max(test_results), average_production(test_results)]
