def triangle_pattern(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end="")
        print()
if __name__ == "__main__":
    triangle_pattern(int(input()))
