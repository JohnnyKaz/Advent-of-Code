"""
https://adventofcode.com/2015/day/13
Advent of Code 2015 - Day 13
--- Knights of the Dinner Table ---
"""

from itertools import permutations
from collections import defaultdict
from numpy import inf

def circular_permutations_directionless(iterable):
    # returns the circular permutations when direction (clockwise/counter-clockwise) doesn't matter (ABCD == ADCB)
    # (n-1)!/2 permutations (check: https://dyclassroom.com/aptitude/circular-permutation)
    out = set()
    for p in permutations(iterable[1:]):
        # is the reverse not already in the set?
        if not p[::-1] in out:
            out.add(p)
            yield (iterable[0],) + p      

def circular_permutations_direction(iterable):
    # returns the circular permutations when direction (clockwise/counter-clockwise) matters (ABCD != ADCB)
    # (n-1)! permutations (check: https://dyclassroom.com/aptitude/circular-permutation)
    for p in permutations(iterable[1:]):
        yield (iterable[0],) + p

def solve(guests):
    final = -inf
    for p in circular_permutations_directionless(list(guests)):
        total = 0
        i, l = 0, len(p)
        while True:
            ii = (i+1) % l
            g = guests[p[i]]
            total += g[p[i-1]] + g[p[ii]]
            i = ii
            if i == 0:
                break
        final = max(final, total)
    return final

with open('input.txt', 'r') as f:
    guests = defaultdict(dict)  # a dictionary of guests, with values: dictionaries of guests and happiness
    for line in f:
        params = line.rstrip('.\n').split(' ')
        happiness = int(params[3]) if params[2] == 'gain' else -int(params[3])
        guests[params[0]][params[-1]] = happiness

    print("Part 1:", solve(guests))
    # add myself as a guest
    others = [g for g in guests]
    for g in others:
        guests['Myself'][g] = guests[g]['Myself'] = 0
    print("Part 2:", solve(guests))