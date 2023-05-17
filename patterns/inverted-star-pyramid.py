def inverted_star_pyramid(n):
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for j in range(n - i):
            print("*", end="")
        for j in range(n - i - 1):
            print("*", end="")
        print()

if __name__ == "__main__":
    inverted_star_pyramid(5)
