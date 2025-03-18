"""
Make Stickers

Time to produce robots! For the correct assembly of robots
on the production line, it is necessary to label the parts,
as different robot components consist of varying numbers of
parts. Therefore, stickers need to be created for each part.

Create a function make_stickers that:

Takes the number of details (details_count) and the name
of the part (robot_part).
Returns a list of strings formatted "{robot_part} detail #{n}",
where n is the detail's number in order.

Examples:

make_stickers(3, "Body")
# ["Body detail #1", "Body detail #2", "Body detail #3"]
make_stickers(4, "Head")
# ["Head detail #1", "Head detail #2", "Head detail #3", "Head detail #4"]
make_stickers(0, "Foot")
# []

"""


def make_stickers(details_count, robot_part):
    return [
        f"{robot_part} detail #{part + 1}"
        for part in range(details_count)
    ]
