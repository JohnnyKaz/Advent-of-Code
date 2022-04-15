# https://adventofcode.com/2015/day/1
with open("input.txt") as f:
    line = f.readline()
    # Part 1:
    floor = 0
    transitions = [1 if i == '(' else -1 for i in line]
    print("Part 1: ", sum(transitions))
    # Part 2:
    for idx, val in enumerate(transitions):
        floor += val
        if floor < 0:
            break
    print("Part 2: ", idx+1)
