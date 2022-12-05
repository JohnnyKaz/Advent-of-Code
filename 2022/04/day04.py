"""
https://adventofcode.com/2022/day/4
Advent of Code 2022 - Day 4
--- Camp Cleanup ---

Program Logic:
For part 1, a complete overlap happens when
  s1----s2~~~~e2---e1     or      s2----s1~~~~e1---e2
(s2-s1)>0 and (e1-e2)>0   or    (s2-s1)<0 and (e1-e2)<0
So, an overlap occurs if the terms (s2-s1), (e1-e2) have the same sign -> (s2-s1)*(e1-e2)>0
To account for the possibility that s1==s2 or/and e1==e2 -> (s2-s1)*(e1-e2)>=0

For part 2, we can have the partial overlaps:
s1----s2----e1---e2       or      s2----s1----e2---e1
    s1<=s2<=e1            or          s2<=s1<=e2
"""

part1, part2 = 0, 0
with open("input.txt") as f:
    for line in f:
        time_list = [time for pair in line.rstrip().split(',') for time in pair.split('-')]
        start1, end1, start2, end2 = tuple(map(int, time_list))
        part1 += (start2 - start1) * (end1 - end2) >= 0
        part2 += start1 <= start2 <= end1 or start2 <= start1 <= end2
        
print("Part 1: ", part1)
print("Part 2: ", part2)