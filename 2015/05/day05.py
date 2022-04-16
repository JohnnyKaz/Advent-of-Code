"""
https://adventofcode.com/2015/day/5
Advent of Code 2015 - Day 5
--- Doesn't He Have Intern-Elves For This? ---
"""

def isNiceStringPt1(str):
    vowels = "aeiou"
    bannedPairs = {'a':'b', 'c':'d', 'p':'q', 'x':'y'}
    vowelCount = 1 if str[0] in vowels else 0
    hasConsecutiveLetter = False

    prev = str[0]
    for curr in str[1:]:
        if prev in bannedPairs.keys() and curr == bannedPairs[prev]:
            return False
        if curr in vowels:
            vowelCount += 1
        if prev == curr:
            hasConsecutiveLetter = True
        prev = curr
    return vowelCount >= 3 and hasConsecutiveLetter 

def isNiceStringPt2(str):
    str2 = str + '\\'
    pprev = str2[0]
    prev = str2[1]
    hasPair = True if str2.find(str[0:2], 2) != -1 else False
    sameBetween = False

    for i, curr in enumerate(str[2:], start=2):
        if curr == pprev:
            sameBetween = True
        if str2.find(str2[i-1:i+1], i+1) != -1:
            hasPair = True
        if hasPair and sameBetween:
            return True
        pprev = prev
        prev = curr
    return False 

with open('input.txt') as f:
    totalNicePt1 = 0
    totalNicePt2 = 0
    for str in f:
        if isNiceStringPt1(str.strip()):
            totalNicePt1 += 1
        if isNiceStringPt2(str.strip()):
            totalNicePt2 += 1
    print("Part 1:", totalNicePt1)
    print("Part 2:", totalNicePt2)
