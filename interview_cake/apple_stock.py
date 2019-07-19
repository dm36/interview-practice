def get_max_profit_n_squared(stock_prices):
    max_diff = -float("inf")
    for i in range(len(stock_prices)):
        for j in range(len(stock_prices)):
            if j > i:
                if stock_prices[j] - stock_prices[i] > max_diff:
                    max_diff = stock_prices[j] - stock_prices[i]
    return max_diff

def get_max_profit_n_squared_better(stock_prices):
    max_diff = -float("inf")
    for i in range(len(stock_prices)):
        for j in range(i + 1, len(stock_prices)):
                if stock_prices[j] - stock_prices[i] > max_diff:
                    max_diff = stock_prices[j] - stock_prices[i]
    return max_diff


# O(n) time, O(1) space
def get_max_profit_fastest(stock_prices):
    max_profit = -float("inf")
    min_price = float("inf")

    # update max profit if current stock price - min price is > the
    # max profit

    # don't need to update the max_price too!

    # update min price if the stock is less than the min price
    for stock in stock_prices:
        max_profit = max(max_profit, stock - min_price)
        min_price = min(stock, min_price)
    return max_profit

print "n^2 solution: "
stock_prices = [10, 7, 5, 8, 11, 9]
print (get_max_profit_n_squared(stock_prices))

print
print "O(n^2) solution better: "
stock_prices = [10, 7, 5, 8, 11, 9]
print (get_max_profit_n_squared_better(stock_prices))

print
print "O(n) solution: "
stock_prices = [10, 7, 5, 8, 11, 9]
print (get_max_profit_fastest(stock_prices))
print

print "O(n) solution: "
stock_prices = [7,6,4,3,1]
print (get_max_profit_fastest(stock_prices))
print
