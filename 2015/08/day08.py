"""
https://adventofcode.com/2015/day/8
Advent of Code 2015 - Day 8
--- Matchsticks ---
"""

def numOfChars(str):
    lenCode = len(str)
    lenMemory = 0
    i = 0
    while i < lenCode:
        if str[i] == '"':
            i += 1
            continue
        elif str[i] == '\\':
            if str[i+1] in ('\\', '"'):
                i += 2
            elif str[i+1] == 'x':
                i += 4
        else:
            i += 1
        lenMemory += 1
    return lenCode - lenMemory

def encodeStr(str):
    lenCode = len(str)
    newStr = ['"']
    for char in str:
        if char == '"':
            newStr.append('\\"')
        elif char == '\\':
            newStr.append('\\\\')
        else:
            newStr.append(char)
    newStr.append('"')
    newStr = ''.join(newStr)
    lenMemory = len(newStr)
    return lenMemory - lenCode



with open('input.txt') as f:
    part1, part2 = 0, 0
    for line in f:
        part1 += numOfChars(line.rstrip())
        part2 += encodeStr(line.rstrip())

# Part 1
print("Part 1:", part1)
# Part 2
print("Part 2:", part2)
