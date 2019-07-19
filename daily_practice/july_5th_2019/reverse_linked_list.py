# 1 -> 2 -> 3
# 3 -> 2 -> 1

# set temp variable to be the head (outside of the while loop)

# inside the while loop

# keep track of what's the next node in the linked list (next variable)
# update next to be the previous
# set previous to be current
# move current to next

def reverse(head_of_list):
    temp = head_of_list
    prev = None

    while temp:
        next = temp.next
        temp.next = prev
        prev = temp
        temp = next

    return prev
