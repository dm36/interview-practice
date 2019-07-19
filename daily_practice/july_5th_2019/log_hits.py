# hash a time to the number of hits

import time
import collections

time_to_hits = collections.defaultdict(int)
# time.time() to get the current time -> incrementing a count of the # of hits
# at that timestamp, key in the hash map is a tuple of minute and a second
def log_hit():
    my_time = int(time.time())
    # print (int(my_time))
    time_to_hits[my_time] += 1

# get hits is going to iterate over the last 5 minutes and increment all the hits
# by going through the hash map
# number of hits in the last 5 minutes
def get_hits():
    my_time = int(time.time())
    print my_time
    five_minutes_ago = my_time - 300
    print five_minutes_ago
    count = 0

    print time_to_hits
    for i in range(five_minutes_ago, my_time + 1):
        print i
        count += time_to_hits[i]

    return count


log_hit()
log_hit()
log_hit()
log_hit()
log_hit()
log_hit()
log_hit()
log_hit()
log_hit()
log_hit()
log_hit()
log_hit()
log_hit()
log_hit()
log_hit()
log_hit()
log_hit()
log_hit()
log_hit()
log_hit()
log_hit()
log_hit()
log_hit()
log_hit()
log_hit()
log_hit()
log_hit()
print time_to_hits
#
print get_hits()
# notes

# 1990, one-page website, want to keep track of people who are visiting it, google analytics,
# keep track of hits to the website

# loghits() function- gets called automatically- using flask, django- everytime someone visits
# a website- gets called once, increment and records a hit

# implement log_hit- gets called every time someone visits the website

# get_hits- doesn't take any parameters, admin page- reporting hits we have gotten, # of hits
# in the last 5 mins

# 1 hit  0:30
# 2 hits 3:00
# 1 hit  4:30
# 1 hit  7:00


# pseudocode

# log_hit- everytime the user goes to the website- we increment a global variable
# for the number of hits

# every 5 minutes that have passed- log_hit sets the number of hits to 0

# get_hits return the global variable that log_hit is updating



#
# Your previous Plain Text content is preserved below:
#
# logHit()
#

#
