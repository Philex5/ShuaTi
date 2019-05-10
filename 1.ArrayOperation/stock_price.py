def stock_price(prices):
    l = len(prices)
    i = 0
    j = 1
    profit = 0
    while j < l:
        if prices[i] < prices[j]:
            profit += prices[j] - prices[i]
        i = j
        j += 1
    print(profit)
    return profit

assert stock_price([7, 1, 5, 3, 6, 4]) == 7
assert stock_price([1, 2, 3, 4, 5]) == 4
assert stock_price([7, 6, 4, 3, 1]) == 0