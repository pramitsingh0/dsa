def star_pyramid(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(i + 1):
            print("*", end="")
        for j in range(i):
            print("*", end="")
        print()

if __name__ == "__main__":
    star_pyramid(int(input()))
