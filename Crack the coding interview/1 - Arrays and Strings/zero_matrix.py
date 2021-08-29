# Write an algorithm such that if there is a 0, in an M X N matrix the entire row and column becomes 0


def zero_matrix(matrix):
    row_check = []
    column_check = []
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[0])):
            if matrix[x][y] == 0:
                row_check.append(x)
                column_check.append(y)

    for m in range(0, len(row_check)):
        for n in range(0, len(matrix[0])):
            matrix[row_check[m]][n] = 0

    for a in range(0, len(matrix)):
        for b in range(0, len(column_check)):
            matrix[a][column_check[b]] = 0

    return matrix


test_matrix = [[1,0,6,5,8], [1,4,9,1,4], [0,2,3,4,5], [1,4,5,2,8], [9,4,2,1,0]]
print(zero_matrix(test_matrix))
