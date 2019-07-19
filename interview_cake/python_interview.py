# -*- coding: utf-8 -*-
# # issue is negative indices- when day is -2 becomes daily_balance[-2:0]
# def show_balances(daily_balances):
#     # do not include -1 because that slice will only have 1 balance, yesterday
#     for day in range(-3, -1):
#         balance_slice = daily_balances[day : day + 2]
#
#         # use positive number for printing
#         print("slice starting %d days ago: %s" % (abs(day), balance_slice))

def show_balances(daily_balances):
    for day in range(len(daily_balances) - 3, len(daily_balances) - 1):
        print day
        balance_slice = daily_balances[day : day + 2]

        # use positive number for printing
        print("slice starting %d days ago: %s" % (abs(day), balance_slice))

daily_balances = [107.92, 108.67, 109.86, 110.15]
show_balances(daily_balances)

# one-liner to count capital characters in a file
# count = sum(character.isupper() for line in fh for character in line)

# fixing shadowing issue- if we instead had self.num_pets += 1
# Turns out, there's the difference between class and instance-
# attributes. When we created rover and added to num_pets, we
# accidentally shadowed Pet.num_pets with rover.num_pets—and
# they're two completely different variables now!

# Our Pet class still thinks there are 0 pets, because each
# new pet adds 1 and shadows the class attribute num_pets
# with its own instance attribute.

# Shadowing being scope

class Pet(object):
    num_pets = 0
    def __init__(self, name):
        self.name = name

        # change from: self.num_pets += 1
        Pet.num_pets += 1

    def speak(self):
        print("My name's %s and the number of pets is %d" % (self.name, self.num_pets))

rover = Pet("Rover")
spot = Pet("Spot")
rover.speak()
spot.speak()


big_num_1 = 1000
big_num_2 = 1000
small_num_1 = 1
small_num_2 = 1

# first one should return False
# second should return True
# reason is is checks equality of objects- pointing
# to the same variable, and in the case of small
# numbers- these are singletons- so brand new object
# isn't created each time for small integers

print big_num_1 is big_num_2
print small_num_1 is small_num_2

question_template = {
    "title": "default title",
    "question": "default question",
    "answer": "default answer",
    "hints": []
}

# issue is this doesn't create a deep copy of a dictionary and the extend carries over
# when you re-run the code- solution- deep copy the dictionary
def make_new_question(title, question, answer, hints=None):
    new_q = question_template.copy()

    # always require title, question, answer
    new_q["title"] = title
    new_q["question"] = question
    new_q["answer"] = answer

    # sometimes there aren't hints, that's fine. Otherwise, add them:
    if hints is not None:
        new_q["hints"].extend(hints)

    return new_q

question_1 = make_new_question("title1", "question1", "answer1", ["q1 hint1", "q1 hint2"])
question_2 = make_new_question("title2", "question2", "answer2")
question_3 = make_new_question("title3", "question3", "answer3", ["q3 hint1"])
print question_1
print question_2
print question_3

# once you use an iterator- you don't get the same #
iterator = (i for i in range(1, 4))
matrix = [[x * y for y in iterator] for x in iterator]
print matrix

# Start with the outer for loop, which is for x in iterator. This is the first time we've called the iterator, so we get x = 1
# Go inside the inner list comprehension to reach our inner for loop, for y in iterator. Since we already called our iterator once before, we get y = 2
# Do our computation, x * y = 2, which is the first value in our first list
# Keep working through the inner for loop, yielding the next value so that y = 3
# Do our computation, where our x is still 1 so x * y = 3, which is the second value in our first list
# Try to keep working through the inner for loop, and that loop ends, since there are no more values in our iterator
# Pop back up to the outer for loop, but the iterator is still empty, so we finish our list comprehension

iterator = [i for i in range(1, 4)]
matrix = [[x * y for y in iterator] for x in iterator]
print matrix
