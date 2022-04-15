"""
https://adventofcode.com/2015/day/4
Advent of Code 2015 - Day 4
--- The Ideal Stocking Stuffer ---
"""
import hashlib

def findMinNumber(key, numOfZeros):
    zeros = "0" * numOfZeros
    i = 1
    while True:
        phrase = key + str(i)
        if hashlib.md5(phrase.encode('utf-8')).hexdigest().startswith(zeros):
            break
        i += 1
    return i

key = "ckczppom"

# Part 1:
num = findMinNumber(key, 5)
print("Part 1:", num)

# Part 2:
num = findMinNumber(key, 6)
print("Part 2:", num)
