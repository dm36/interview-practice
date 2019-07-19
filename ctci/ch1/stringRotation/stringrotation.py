def isRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    elif s2 in s1 + s1:
        return True
    else:
        return False

# Checking if s2 is a rotation of s1
print isRotation("waterbottle", "erbottlewat")
print isRotation("dog", "cat")
