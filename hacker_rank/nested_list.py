lst = []

# Build a nested list with a person's score and name
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    lst.append([score, name])
    print lst

# Sort the nested list by score
lst.sort()
print lst

# Find the second min score
min_score = lst[0][0]
second_min_score = float("inf")
for score, name in lst:
    if score > min_score:
        second_min_score = score
        break
print second_min_score

# Get the name of the people with the second min score
people = []
for score, name in lst:
    if score == second_min_score:
        people.append(name)

# Print them out
people.sort()
for person in people:
    print person

# marksheet = []
# for _ in range(0,int(input())):
#     marksheet.append([input(), float(input())])
#
# second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
# print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
