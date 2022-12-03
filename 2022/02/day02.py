"""
https://adventofcode.com/2022/day/2
Advent of Code 2022 - Day 2
--- Rock Paper Scissors ---

Program Logic:
Encode each move as a number (rock=0, paper=1, scissors=2)
The moves needed to achieve each outcome (loss, draw, win)
are stored in the outcomes list
"""

# outcomes: what to pick to get the outcome 
# outcomes = (loss, draw, win)
# 0: Rock,      1: Paper,       2: Scissors
# e.g. if opponent chose Rock (0) and we want to lose -> choose outcomes[0][0] = 2 (Scissors)
outcomes = ((2, 0, 1), (0, 1, 2), (1, 2, 0))

def characterScore(char1, char2):
    return ord(char1) - ord(char2)

def calcScore(opponent, me, isPart2):
    """
    opponent: move played by the opponent ('A':Rock, 'B':paper, 'C':scissors)
    me: 
        - part 1: move played by me ('X':rock, 'Y':paper, 'Z':scissors)
        - part 2: desired outcome   ('X':loss, 'Y':draw,  'Z':win)
    """
    opponent, me = characterScore(opponent, 'A'), characterScore(me, 'X')
    if isPart2:
        me = outcomes[me][opponent]
    score = me + 1
    score += 3 if me == opponent else 6 if me == outcomes[2][opponent] else 0
    return score

with open("input.txt") as f:
    score, score2 = 0, 0
    for line in f:
        opponent, me = line.split()
        score += calcScore(opponent, me, False)
        score2 += calcScore(opponent, me, True)
print("Part 1: ", score)
print("Part 2: ", score2)