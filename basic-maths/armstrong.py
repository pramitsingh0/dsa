def length(x):
    count = 0
    while x > 0:
        count += 1
        x //= 10
    return count
def armstrong_num(x):
    num_digits = length(x)
    temp = x
    sum = 0
    while x > 0:
        sum += (x % 10) ** num_digits
        x //= 10
    return sum == temp
print(armstrong_num(453))
