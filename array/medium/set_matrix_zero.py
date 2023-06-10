def zeroMatrix(matrix, n, m):
    zero_row = [0] * n
    zero_column = [0] * m
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                zero_row[i] = 1
                zero_column[j] = 1

    for i in range(n):
        for j in range(m):
            if zero_row[i] or zero_column[j]:
                matrix[i][j] = 0
    return matrix


def zeroMatrixEfficient(matrix, n, m):
    row_zero = 1
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                if i == 0:
                    row_zero = 0
                else:
                    matrix[i][0] = 0
                matrix[0][j] = 0
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


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    n = len(matrix)
    m = len(matrix[0])
    ans = zeroMatrixEfficient(matrix, n, m)

    for row in ans:
        for ele in row:
            print(ele, end=" ")
        print()
