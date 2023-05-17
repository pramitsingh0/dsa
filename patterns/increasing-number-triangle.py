def increasing_number_triangle(n):
    currentNum = 1
    for i in range(n):
        for j in range(i + 1):
            print(currentNum, end=" ")
            currentNum += 1
        print()
increasing_number_triangle(5)
