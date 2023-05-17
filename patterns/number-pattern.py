def number_pattern(n):
    for i in range(2 * n - 1):
        for j in range(2 * n - 1):
            if j >= i and j <= 2 * n - i:
                print(i, end="");
                continue
            print(j, end="")
        print()

number_pattern(4)
