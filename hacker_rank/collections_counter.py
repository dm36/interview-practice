from collections import Counter

# https://docs.python.org/2/library/collections.html#collections.Counter

# 10 // number of shoes
# 2 3 4 5 6 8 7 6 5 18 //shoe sizes in the shoe shop
# 6 // number of customers
# 6 55 // shoe size and price
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50

shoes = raw_input()
shoe_sizes = raw_input().split(" ")
customers = int(raw_input())
shoe_size_count = Counter(shoe_sizes)

i = 0
money = 0

while i < customers:
    i += 1

    shoe_size, price = raw_input().split(" ")

    if shoe_size_count[shoe_size] == 0:
        continue
    else:
        money += int(price)
        shoe_size_count[shoe_size] -= 1

print money
