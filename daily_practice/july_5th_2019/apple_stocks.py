# def get_max_profit(stock_prices):
#     max_profit = float('-inf')
#     for i in range(len(stock_prices)):
#         for j in range(len(stock_prices)):
#             if i != j:
#                 max_profit = max(max_profit, stock_prices[j] - stock_prices[i])
#     return max_profit

def get_max_profit(stock_prices):
    max_profit = float("-inf")
    for i in range(len(stock_prices)):
        for j in range(i, len(stock_prices)):
            max_profit = max(max_profit, stock_prices[j] - stock_prices[i])
    return max_profit

# keep track of the minimum stock price observed thus far
# take the difference between the current price and the min price
# observed thus far and update the max profit accordingly

def get_max_profit(stock_prices):
    max_profit = float("-inf")
    min_price = float("inf")

    for i in range(len(stock_prices)):
        max_profit = max(stock_prices[i] - min_price, max_profit)
        min_price = min(stock_prices[i], min_price)

    return max_profit


stock_prices = [10, 7, 5, 8, 11, 9]
print (get_max_profit(stock_prices))

def get_max_profit(stock_prices):
    if len(stock_prices) == 0 or len(stock_prices) == 1:
        raise Exception("Invalid input!")
    max_profit = float("-inf")
    min_price = float("inf")

    for i in range(len(stock_prices)):
        max_profit = max(stock_prices[i] - min_price, max_profit)
        min_price = min(stock_prices[i], min_price)

    return max_profit


# Tests
#
# import unittest
#
# class Test(unittest.TestCase):
#
#     def test_price_goes_up_then_down(self):
#         actual = get_max_profit([1, 5, 3, 2])
#         expected = 4
#         self.assertEqual(actual, expected)
#
#     def test_price_goes_down_then_up(self):
#         actual = get_max_profit([7, 2, 8, 9])
#         expected = 7
#         self.assertEqual(actual, expected)
#
#     def test_price_goes_up_all_day(self):
#         actual = get_max_profit([1, 6, 7, 9])
#         expected = 8
#         self.assertEqual(actual, expected)
#
#     def test_price_goes_down_all_day(self):
#         actual = get_max_profit([9, 7, 4, 1])
#         expected = -2
#         self.assertEqual(actual, expected)
#
#     def test_price_stays_the_same_all_day(self):
#         actual = get_max_profit([1, 1, 1, 1])
#         expected = 0
#         self.assertEqual(actual, expected)
#
#     def test_error_with_empty_prices(self):
#         with self.assertRaises(Exception):
#             get_max_profit([])
#
#     def test_error_with_one_price(self):
#         with self.assertRaises(Exception):
#             get_max_profit([1])
#
#
# unittest.main(verbosity=2)
