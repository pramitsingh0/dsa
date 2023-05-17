def rectangular_star_pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()

if __name__ == "__main__":
    rectangular_star_pattern(int(input()))
