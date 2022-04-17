"""
https://adventofcode.com/2015/day/6
Advent of Code 2015 - Day 6
--- Probably a Fire Hazard ---
"""
import numpy as np

grid = np.full((1000, 1000), False)
grid2 = np.zeros((1000, 1000), dtype=int)

actions  = {'off': lambda x: False, 'on': lambda x: True, 'toggle': lambda x: np.invert(x)}
actions2 = {'off': lambda x: (x-1).clip(0), 'on': lambda x: x+1, 'toggle': lambda x: x+2}

def preprocessInstr(line):
    instr = line.rstrip().split()
    if instr[0] == 'turn':
            instr.pop(0)
    instr[1], instr[2] = instr[1].split(',')
    instr.append('')
    instr[3], instr[4] = instr[3].split(',')
    #instr[2] = instr[2].replace(',', ':')
    return instr

with open('input.txt') as f:
    for line in f:
        instr = preprocessInstr(line)
        a, c, b, d = int(instr[1]), int(instr[2]), int(instr[3])+1, int(instr[4])+1
        grid[a:b, c:d]  = actions[instr[0]](grid[a:b, c:d])
        grid2[a:b, c:d] = actions2[instr[0]](grid2[a:b, c:d])

print("Part 1:", grid.sum())
print("Part 2:", grid2.sum())
