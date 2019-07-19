from itertools import combinations
# shrub is a football coach
# team of P students
# N students to pick from
# ith student has a skill rating S_i
# P students all have the same skill
# rating
# 1 hour of coaching to increase
# skill rating of any student by 1
# min # of hours of coaching before
# able to pick a fair team

# first line # of test cases T
# two integers N and P- # of students
# number of students you need to pick
# N integers (S_i) skill

# Output one line containing Case #x: y where
# x is the test case number and y is the
# min # of hours of coaching before you pick
# a fair team of P students

# Time required to make a fair team is
# Σ(max(Si, Si+1... SP) - Si) for all students
# 1 to P in the team, goal is to minimize this value

# all subsets of P students from the N students
# nCp such subsets- minimizing this value
# so factorial runtime

def training(skills, p, t):
    # build combinations of length p from the skills
    # array- convert each combination to a list,
    # retrieve the largest and take the cumulative difference
    # between the max and each number
    min_diff = float("inf")
    for comb in combinations(skills, p):
        diff = 0
        lst = list(comb)
        max_skill = max(lst)

        for skill in lst:
            diff += max_skill - skill

        if diff < min_diff:
            min_diff = diff

    print ("Case #" + str(t) + ": " + str(min_diff))

t = int(input())
for i in range(t):
    # Array of characters of the input- then
    # cast to integers
    # print (input().split())
    n, p = map(int, input().split())

    # https://stackoverflow.com/questions/1303347/getting-a-map-to-return-a-list-in-python-3-x
    skills = list(map(int, input().split()))
    training(skills, p, i + 1)

# once we fix student with highest level x
# choose students with skills as high as possible
# but less than or equal to x

# sort skill levels in decreasing order
# iterate over each student and assume they have
# the highest value in the team
