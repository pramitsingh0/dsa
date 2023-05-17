def decreasing_letter(n):
    for i in range(n):
        for j in range(n, i, -1):
            print(chr(ord('A') + n - j), end="")
        print()

decreasing_letter(5)
