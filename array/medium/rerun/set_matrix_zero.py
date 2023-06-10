def setMatrixZero(matrix):
    row_zero = 1
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                if i == 0:
                    row_zero = 0
                else:
                    matrix[0][j] = 0
                matrix[i][0] = 0
    for i in range(1, n):
        for j in range(1, m):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0
    if matrix[0][0] == 0:
        for i in range(n):
            matrix[i][0] = 0
    if row_zero == 0:
        for j in range(m):
            matrix[0][j] = 0

    return matrix


print(setMatrixZero([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
