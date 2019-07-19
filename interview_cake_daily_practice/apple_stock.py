# O(n) time, O(1) space
def get_max_profit(stock_prices):
    min_price = float("inf")
    max_profit = 0

    # if the current stock price - the minimum observed price
    # thus far is > than the max profit update it

    # if the stock is less than the min price update min price

    # note that we do this in that order- otherwise we could get
    # ourselves into a situation where we subtract the stock with itself
    for stock in stock_prices:
        max_profit = max(stock - min_price, max_profit)
        min_price = min(stock, min_price)

    return max_profit

print get_max_profit([7, 1, 5, 3, 6, 4])
print get_max_profit([10, 7, 5, 8, 11, 9])
print get_max_profit([7, 6, 4, 3, 1])
