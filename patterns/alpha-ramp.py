def alpha_ramp(n):
    for i in range(n):
        for j in range(i + 1):
            print(chr(ord('A') + i), end='')
        print()

alpha_ramp(5)
