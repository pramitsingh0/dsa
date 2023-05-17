def alpha_hill(n):
    for i in range(n):
        for j in range(n - i, 0, -1):
            print(" ", end="")
        for j in range(i + 1):
            print(chr(ord('A') + j), end="")
        for j in range(i , 0, -1):
            print(chr(ord('A') + j - 1), end="")
        print()

alpha_hill(5)
