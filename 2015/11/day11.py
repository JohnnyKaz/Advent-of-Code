"""
https://adventofcode.com/2015/day/11
Advent of Code 2015 - Day 11
--- Corporate Policy ---
"""

def str_increment(s):
# increments a string of lowercase chars. when 'zz...z' is reached -> wrap around to 'aa...a'
    new = ''
    while s:
        s, c = s[:-1], s[-1]
        if c != 'z':
            new = chr(ord(c) + 1) + new
            break
        else:
            new = 'a' + new
    s = s + new
    #print(s)
    return s

def is_consecutive_char(curr, prev):
    return ord(curr) == ord(prev) + 1

def is_pair(curr, prev):
    return ord(curr) == ord(prev)

def check_pass(s):
    banned_letters = {'i', 'o', 'l'}
    pairs, overlapping_pairs, consecutive_len = 0, 0, 1
    consecutive_condition = False

    if s[0] in banned_letters:
        return False
    prev = s[0]
    for c in s[1:]:
        if c in banned_letters:
            return False
        consecutive_len = consecutive_len+1 if is_consecutive_char(c, prev) else 1
        if consecutive_len >= 3:
            consecutive_condition = True
        if is_pair(c, prev) and not overlapping_pairs:
            pairs += 1
            overlapping_pairs += 2
        overlapping_pairs = max(0, overlapping_pairs-1)
        prev = c
    return consecutive_condition and pairs >= 2

def solve(p):
    while not check_pass(p):
        p = str_increment(p)
    return p

password = 'vzbxkghb'
p1 = solve(password)
print("Part 1:", p1)
print("Part 2:", solve(str_increment(p1)))