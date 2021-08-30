# Rotate a 4 x 4 Matrix 90 degrees:

# [A B C D] [M I E A]
# [E F G H] [N J F B]
# [I J K L] [O K G C]
# [M N O P] [P L H D]


def matrix_rotator(matrix):
    side_one = []
    side_two = []
    side_three = []
    side_four = []
    new_matrix = []
    for x in range(3, -1, -1):
        side_one.append(matrix[x][0])
        side_two.append(matrix[x][1])
        side_three.append(matrix[x][2])
        side_four.append(matrix[x][3])
    new_matrix.append(side_one)
    new_matrix.append(side_two)
    new_matrix.append(side_three)
    new_matrix.append(side_four)
    return new_matrix


matrix = [
    ["a", "b", "c", "d"],
    ["e", "f", "g", "h"],
    ["i", "j", "k", "l"],
    ["m", "n", "o", "p"],
]

print(matrix_rotator(matrix))
