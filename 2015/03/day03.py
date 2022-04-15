# https://adventofcode.com/2015/day/3

import numpy as np

with open("input.txt") as f:
    line = f.readline()    
    moves = {'^':[0,1], 'v':[0,-1], '>':[1,0], '<':[-1,0]}

    # Part 1:
    currPos = np.array([0,0])
    visited = set()
    visited.add(tuple(currPos))
    for c in line:
        currPos += moves[c]
        visited.add(tuple(currPos))
    print("Part 1:", len(visited))

    # Part 2:
    currPositions = np.array([[0, 0], [0, 0]])
    visited = set()
    visited.add(tuple(currPositions[0]))
    index = 0
    for c in line:
        currPositions[index] += moves[c]
        visited.add(tuple(currPositions[index]))
        index = (index + 1) % 2
    print("Part 2:", len(visited))