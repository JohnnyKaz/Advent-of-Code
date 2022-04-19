"""
https://adventofcode.com/2015/day/7
Advent of Code 2015 - Day 7
--- Some Assembly Required ---
"""
import numpy as np

m16 = lambda x: x & 0xFFFF
instructions = {}
values = {} # store numeric values when found, for memoization

def preprocessInstr(line):
    args, res = line.rstrip().split(' -> ')
    args = args.split(' ')
    l = len(args)
    if l == 1:      # only move commands have 1 argument (e.g. 123 -> x)
        instructions[res] = ('MOVE', args[0])  # res : ('MOVE', arg)
        if args[0].isdigit():
            values[res] = m16(int(args[0]))
    elif l == 2:    # only not commands have 2 arguments (e.g. NOT y -> i)
        instructions[res] = ('NOT', args[1])    # res : ('NOT', arg)
    else:
        if args[1] == 'LSHIFT' or args[1] == 'RSHIFT':
            args[2] = int(args[2])
        instructions[res] = (args[1], args[0], args[2])

def recursiveSolve(res):
    if res.isdigit():
        return m16(int(res))
    if res in values:
        return values[res]
    opcode, *args = instructions[res]
    if opcode == 'MOVE':
        ans = recursiveSolve(args[0])
    if opcode == 'NOT':
        ans = ~recursiveSolve(args[0])
    elif opcode == 'AND':
        ans = recursiveSolve(args[0]) & recursiveSolve(args[1])
    elif opcode == 'OR':
        ans = recursiveSolve(args[0]) | recursiveSolve(args[1])
    elif opcode == 'LSHIFT':
        ans = recursiveSolve(args[0]) << args[1]
    elif opcode == 'RSHIFT':
        ans = recursiveSolve(args[0]) >> args[1]
    values[res] = m16(ans)
    return m16(ans)



with open('input.txt') as f:
    for line in f:
        preprocessInstr(line)

# Part 1
a_part1 = recursiveSolve('a')
print("Part 1:", a_part1)

# Part 2
values = {'b':a_part1} # reset the values
print("Part 2:", recursiveSolve('a'))
