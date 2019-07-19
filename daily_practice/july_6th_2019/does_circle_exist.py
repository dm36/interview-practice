# idea is to correlate each instruction with a x, y coordinate move
# and check to see if after completing the instructions- we return
# back to the original (x, y)

# if so => circle
# if not => not circle

def simulate(comm):
    r_mapping = {'n' : 'e', 's': 'w', 'e': 's', 'w': 'n'}
    l_mapping = {'n' : 'w', 's': 'e', 'e': 'n', 'w': 's'}

    x, y, i = 0, 0, 0
    orientation = 'n'

    # repeat the command 50 times and if x and y equals 0 =>
    # we have ourselves a circle
    while i < 10:
        robot_command = comm
        for instruction in robot_command:
            if orientation == 'n' and instruction == 'G':
                y += 1
            elif orientation == 's' and instruction == 'G':
                y -= 1
            elif orientation == 'e' and instruction == 'G':
                x += 1
            elif orientation == 'w' and instruction == 'G':
                x -= 1
            elif instruction == 'R':
                orientation = r_mapping[orientation]
            elif instruction == 'L':
                orientation = l_mapping[orientation]
        i += 1
        if x == 0 and y == 0:
            return 'YES'

    return 'NO'

def doesCircleExist(command):
    return_array = []

    for comm in command:
        return_array.append(simulate(comm))

    return return_array


print doesCircleExist(['RG'])
print doesCircleExist(['G', 'L'])
print doesCircleExist(['GRGL'])
print doesCircleExist(['GGGGR', 'RGL'])
