def pascalsTriangleVarOne(r, c):
    n = r - 1
    r = c - 1
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res


print(pascalsTriangleVarOne(5, 3))


def pascalsTriangleVarTwo(n):
    res = []
    for i in range(n):
        if i == 0:
            res.append(1)
        else:
            res.append(res[-1] * (n - i) // i)
    return res


print(pascalsTriangleVarTwo(5))


def pascalsTriangleVarThree(n):
    res = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0:
                row.append(1)
            else:
                row.append(row[-1] * ((i + 1) - j) // j)
        res.append(row)
    return res


print(pascalsTriangleVarThree(5))
