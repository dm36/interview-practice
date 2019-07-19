import math

def lesser_of_two_evens(a, b):
    if a % 2 == 1 or b % 2 == 1:
        return max(a, b)
    else:
        return min(a, b)

# def lesser_of_two_evens(a,b):
#     if a%2 == 0 and b%2 == 0:
#         return min(a,b)
#     else:
#         return max(a,b)

print (lesser_of_two_evens(2, 4))
print (lesser_of_two_evens(2, 5))
print

def animal_crackers(text):
    first_letters = ([word[0] for word in text.split()])
    if first_letters[0] == first_letters[1]:
        return True
    return False

# def animal_crackers(text):
#     wordlist = text.split()
#     return wordlist[0][0] == wordlist[1][0]

print (animal_crackers('Levelheaded Llama'))
print (animal_crackers('Crazy Kangaroo'))
print

def makes_twenty(n1, n2):
    if n1 + n2 == 20 or n1 == 20 or n2 == 20:
        return True
    return False

# def makes_twenty(n1,n2):
#     return (n1+n2)==20 or n1==20 or n2==20

print (makes_twenty(20, 10))
print (makes_twenty(12, 8))
print (makes_twenty(2, 3))
print

def old_macdonald(name):
    return name[0].upper() + name[1:3] + name[3].upper() + name[4:]


# def old_macdonald(name):
#     if len(name) > 3:
#         return name[:3].capitalize() + name[3:].capitalize()
#     else:
#         return 'Name is too short!'
# .capitalize()!

print (old_macdonald('macdonald'))
print

def master_yoda(text):
    arr = text.split()
    arr.reverse()
    return ' '.join(arr)

# def master_yoda(text):
#     return ' '.join(text.split()[::-1])

print (master_yoda('I am home'))
print (master_yoda('We are ready'))
print

def almost_there(n):
    if abs(n - 100) <= 10 or abs(n - 200) <= 10:
        return True
    return False

# def almost_there(n):
#     return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
print (almost_there(90))
print (almost_there(104))
print (almost_there(150))
print (almost_there(209))
print

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

# def has_33(nums):
#     for i in range(0, len(nums)-1):
#
#         # nicer looking alternative in commented code
#         #if nums[i] == 3 and nums[i+1] == 3:
#
#         if nums[i:i+2] == [3,3]:
#             return True
#
#     return False

print (has_33([1, 3, 3]))
print (has_33([1, 3, 1, 3]))
print (has_33([3, 1, 3]))
print
# print (has_33([1, 3, 1, 3]))
# print (has_33([3, 1, 3]))

def paper_doll(text):
    final_str = ""
    for char in text:
        final_str += (char * 3)
    return final_str

# def paper_doll(text):
#     result = ''
#     for char in text:
#         result += char * 3
#     return result
print (paper_doll('Hello'))
print (paper_doll('Mississippi'))
print

# def is_prime(num):
#     for i in range(3, int(math.sqrt(num)) + 1, 2):
#         if num % i == 0:
#             return False
#     return True

# if sum is <= 21 => return sum
# if sum > 21 and there's a 11 => reduce
# sum by 10
# if sum exceeds 21 => return "BUST"

def blackjack(a, b, c):
    sum = a + b + c
    if sum <= 21:
        return sum
    elif sum > 21 and (a == 11 or b == 11 or c == 11):
        sum -= 10
        return sum
    elif sum > 21:
        return 'BUST'

# def blackjack(a,b,c):
#
#     if sum((a,b,c)) <= 21:
#         return sum((a,b,c))
#     elif sum((a,b,c)) <=31 and 11 in (a,b,c):
#         return sum((a,b,c)) - 10
#     else:
#         return 'BUST'

print (blackjack(5, 6, 7))
print (blackjack(9, 9, 9))
print (blackjack(9, 9, 11))
print

def summer_69(arr):
    no_sum_flag = False
    sum = 0
    for num in arr:
        if num == 6:
            no_sum_flag = True
        if no_sum_flag == False:
            sum += num
        elif num == 9:
            no_sum_flag = False
    return sum

# def summer_69(arr):
#     total = 0
#     add = True
#     for num in arr:
#         while add:
#             if num != 6:
#                 total += num
#                 break
#             else:
#                 add = False
#         while not add:
#             if num != 9:
#                 break
#             else:
#                 add = True
#                 break
#     return total

print "Summer of 69"
print summer_69([1, 3, 5])
print summer_69([4, 5, 6, 7, 8, 9])
print summer_69([2, 1, 6, 9, 11])
print

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def count_primes(num):
    count = 0
    for i in range(2, num):
        if is_prime(i):
            print (i)
            count += 1
    return count

# def count_primes(num):
#     primes = [2]
#     x = 3
#     if num < 2:  # for the case of num = 0 or 1
#         return 0
#     while x <= num:
#         for y in range(3,x,2):  # test all odd factors up to x-1
#             if x%y == 0:
#                 x += 2
#                 break
#         else:
#             primes.append(x)
#             x += 2
#     print(primes)
#     return len(primes)

print (count_primes(100))
print
