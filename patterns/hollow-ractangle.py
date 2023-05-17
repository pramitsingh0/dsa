def hollow_rectangle(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            for j in range(n):
                print("*", end="")
            print()
            continue
        for j in range(n):
            if j == 0 or j == n - 1:
                print('*', end="")
                continue
            print(" ", end="")
        print()

hollow_rectangle(1)
