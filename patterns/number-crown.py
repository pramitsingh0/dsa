def number_crown(n):
    for i in range(n):
        for j in range(1, i + 2):
            print(j, end="")
        for j in range(n - i - 1):
            print("  ", end="")
        for j in range(i + 1, 0, -1):
            print(j, end="")
        print()

number_crown(5)
