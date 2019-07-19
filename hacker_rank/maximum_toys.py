def maximumToys(prices, k):
    count = 0
    money_spent = 0
    prices.sort()

    for price in prices:
        if money_spent + price > k:
            return count
        else:
            money_spent += price
            count += 1




print maximumToys([1, 12, 5, 111, 200, 1000, 10], 50)
