def pascalsTriangleVarOne(r, c):
    n = r - 1
    r = c - 1
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res / (i + 1)
    print(res)

def pascalsTriangleVarTwo(n):
    res = []
    for i in range(n):
        if i == 0:
            res.append(1)
        else:
            res.append(res[-1] * (n - i) // i)
    return res

def pascalsTriangleVarThree(n):
    res = []
    for i in range(1, n + 1):
        res.append(pascalsTriangleVarTwo(i))
    return res
def pascalsTriangleVarFour(n):
    res = [[1]]
    for i in range(n):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(temp) - 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res

def pascalsTriangleFinal(n):
    res = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0:
                row.append(1)
            else:
                curr_ele = row[-1] * (i + 1 - j) // j
                row.append(curr_ele)
        res.append(row)
    return res
print(pascalsTriangleVarOne(5, 3))
print(pascalsTriangleVarFour(6))
print(pascalsTriangleFinal(6))