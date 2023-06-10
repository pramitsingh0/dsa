def buySell(prices):
    min = None
    max_profit = 0
    for i in range(len(prices)):
        if min == None or prices[i] < min:
            min = prices[i]
        else:
            if prices[i] - min > max_profit:
                max_profit = prices[i] - min
    return max_profit


print(buySell([7, 6, 4, 3, 1]))
