def diamond_star(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(i + 1):
            print("*", end="")
        for j in range(i):
            print("*", end="")
        print()
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for j in range(n - i):
            print("*", end="")
        for j in range(n - i - 1):
            print("*", end="")
        print()


diamond_star(5)
