#!usr/bin/env python3
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# |_|_|
# |_|_| -> |_| -> 2 1
#                 1 0
# |_|    3 1
# |_| -> 2 1
#        1 0
#
# |_|_| ->  3 2 1
#           1 1 0
#
# |_|_|    6 3 1
# |_|_| -> 3 2 1
#          1 1 0
#
#             20 10 04 01
# |_|_|_|     10 06 03 01
# |_|_|_| ->  04 03 02 01
# |_|_|_|     01 01 01 00
# So the number of paths at each edge is = # of paths of number below it and # of paths to the right,
# Now we set it up in reverse since arrays read from left to right, and the answer will be the same.
# Ex:
#             01 04 10 20
# |_|_|_|     01 03 06 10
# |_|_|_| ->  01 02 03 04
# |_|_|_|     00 01 01 01
#
# TODO: Finish later


def grid_path_calculator():
    pass
