def buy_sell(prices):
    min = None
    max_profit = 0
    for i in range(len(prices)):
        if min == None or prices[i] < min:
            min = prices[i]
        else:
            if prices[i] - min >= max_profit:
                max_profit = prices[i] - min
    return max_profit


print(buy_sell([7, 1, 5, 3, 6, 4]))
