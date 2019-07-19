list2 = [(2, 4), (6, 8), (10, 12)]
for tup in list2:
    print (tup)

for num1, num2 in list2:
    print (num1, num2)

d = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d:
    print (item)

print (list(d.keys()))
print (sorted(d.values()))

x = 0
while x < 10:
    print ('x is currently', x)
    print (' x is less than 10, adding 1 to x')
    x += 1

else:
    print ('All Done!')


x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('Breaking because x==3')
        break
    else:
        print('continuing...')
        continue
