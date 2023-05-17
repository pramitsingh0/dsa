def sum(N):
    if N == 1:
        return 1
    return N + sum(N - 1)


print(sum(5))
