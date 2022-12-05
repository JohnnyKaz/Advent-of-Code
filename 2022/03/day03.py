"""
https://adventofcode.com/2022/day/3
Advent of Code 2022 - Day 3
--- Rucksack Reorganization ---

Program Logic:
I treat the given rucksacks as sets of item types and I need to find the intersection between them.
In the problem, it is guaranteed that the intersection has only 1 element -> calculate the score 
- part A: split each rucksack into two compartments and find the intersection of them
- part B: find the intersection between each group of 3 elves
"""
from collections import Counter
from more_itertools import windowed

def charScore(c):
    return ord(c) - ord('A') + 27 if c.isupper() else ord(c) - ord('a') + 1

def main():
    with open("input.txt") as f:
        rucksacks = f.read().split('\n')
    # part A
    score = sum([charScore(c) for rsack in rucksacks for c in set(rsack[len(rsack)//2:]).intersection(rsack[:len(rsack)//2])])
    print("Part 1: ", score)
    # part B
    windows = list(windowed(rucksacks, n=3, step=3))
    score = sum([charScore(*set(group1).intersection(group2, group3)) for group1, group2, group3 in windows])
    print("Part 2: ", score)

if __name__ == "__main__":
  main()