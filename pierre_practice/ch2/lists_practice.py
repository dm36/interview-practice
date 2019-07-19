my_list = ['one', 'two', 'three', 4, 5]
print (my_list + ['add new item'])
print (my_list)

# permanent addition
my_list = my_list + ['add new item']
print (my_list)

# double the list
print (my_list * 2)

new_list = [5, 4, 3, 6]

# sort and reverse are in-place
new_list.sort()
print (new_list)

new_list.reverse()
print (new_list)

lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
lst_3 = [7, 8, 9]

matrix = [lst_1, lst_2, lst_3]
print (matrix)
print (matrix[0])
print (matrix[0][0])

print ([row[1] for row in matrix])
