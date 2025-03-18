"""
Get Location

Our robots can now convert motion commands into actual movement:

"forward" means y + 1.
"back" means y - 1.
"right" means x + 1.
"left" means x - 1 .

But they still need GPS, which... isn't ideal. To circumvent it,
create the get_location function that:

Takes two parameters:
coordinates — a list of initial coordinates formatted as [x, y].
commands — a list of movement commands like ["command1", "command2", "command3" ...].
Returns a list of coordinates [x, y]
achieved after commands are performed.
For example, we have the coordinates = [2, 1]
and commands = ["left", "back", "back"] lists:

Coordinates after the first command — [1, 1] (1 step left).
Coordinates after the second command — [1, 0] (1 step back).
Coordinates after the third command — [1, -1] (1 step back).
Result is the [1, -1] list.

Other examples:
get_location([0, 0], ["forward", "right"])  # [1, 1]
get_location([2, 3], ["back", "back", "back", "right"])  # [3, 0]
get_location([0, 5], ["back", "back", "back", "right", "left", "forward"])  # [0, 3]
"""


def get_location(coordinates, commands):
    x, y = coordinates

    for command in commands:
        if command == "forward":
            y += 1
        elif command == "back":
            y -= 1
        elif command == "right":
            x += 1
        elif command == "left":
            x -= 1

    return [x, y]
