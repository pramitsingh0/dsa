def nto1(n):
    if n == 1:
        return print(1)
    print(n)
    return nto1(n - 1)

nto1(5)
