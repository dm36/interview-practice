def missing_ranges(vals):
    final_arr = []
    if len(vals) == 0:
        return ['0->99']
    for i in range(1, len(vals)):
        if vals[i] == vals[i-1] + 1:
            continue
        elif vals[i] == vals[i-1] + 2:
            final_arr.append(str(vals[i-1] + 1))
        else:
            final_arr.append(str(vals[i-1] + 1) + '->' + str(vals[i] - 1))

    final_arr.append(str(vals[-1] + 1) + '->' + '99')
    print final_arr


missing_ranges([0, 1, 3, 50, 75])
