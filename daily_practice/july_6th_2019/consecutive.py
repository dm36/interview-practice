# pseudocode:

# start at numbers between 1 and the final number
# (this corresponds to the start number)

# add consecutive numbers starting from the start number
# until you either arrive at the target or you go past the target

# if you arrive at the target increment a number of ways

# at some point you'll arrive at a number at which point adding any future
# consecutive number will go past num => we can break out

def consecutive(num):
    count = 0
    for start_num in range(1, num):
        total = start_num
        if start_num + (start_num + 1) > num:
            break
        for consecutive_num in range(start_num + 1, num):
            total += consecutive_num
            if total == num:
                count += 1
                break
    return count

print consecutive(21)
