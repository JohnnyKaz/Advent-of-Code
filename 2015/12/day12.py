"""
https://adventofcode.com/2015/day/12
Advent of Code 2015 - Day 12
--- JSAbacusFramework.io ---
"""

import re
from collections import deque

def count_all_nums(txt):
    x = re.findall(r'-?\d+', txt)
    y = map(int, x)
    return sum(y)

def remove_reds(txt):
    # parse the text and remove all {...} with value "red" and their children
    stack = deque()
    i = 0
    while i < len(txt):
        c = txt[i]
        if c == '{':
            stack.append(i)
        elif c == '}' and stack:
            start = stack.pop()
            if re.search(r':"red"', txt[start:i]):
                txt = txt[:start] + txt[i+1:]
                i = start - 1
        i += 1
    return txt

with open('input.txt', 'r') as f:
    txt = f.read()    
    print("Part 1:", count_all_nums(txt))
    print("Part 2:", count_all_nums(remove_reds(txt)))