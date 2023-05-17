def alpha_triangle(n):
    for i in range(n):
        for j in range(i + 1, 0, -1):
            print(chr(ord('A') + n - j), end=" ")
        print()
alpha_triangle(5)
