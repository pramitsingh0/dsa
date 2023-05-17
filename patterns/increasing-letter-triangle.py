def increasing_letter(n):
    for i in range(n):
        for j in range(i + 1):
            print(chr(ord('A') + j), end="")
        print()

increasing_letter(5)
