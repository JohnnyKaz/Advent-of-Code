"""
https://adventofcode.com/2015/day/10
Advent of Code 2015 - Day 10
--- Elves Look, Elves Say ---
"""

digits = '0123456789'

def lookAndSay(initial, iterations):
    previous = str(initial)
    for i in range(iterations):
        current = []
        count = 1
        ch1 = previous[0]
        for ch2 in previous[1:]:
            if ch2 == ch1:
                count += 1
                continue
            # maybe check that count <= 10 
            current.append(digits[count])
            current.append(ch1)
            ch1 = ch2
            count = 1
        current.append(digits[count])
        current.append(ch1)
        previous = ''.join(current)
    return len(previous)

print("Part 1:", lookAndSay(3113322113, 40))
print("Part 2:", lookAndSay(3113322113, 50))
