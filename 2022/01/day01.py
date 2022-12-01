# https://adventofcode.com/2022/day/1
"""
Program Logic:
- create a max heap with the calories per elf -> O(n*log(n))
- get the sum of the k=3 highest elements -> O(k*log(n))
overall complexity: O(n*log(n))
"""
import heapq

heap = []

def calc_n_max(n):
    res = 0
    for i in range(n):
        res += heapq.heappop(heap)
    return -1 * res

with open("input.txt") as f:
    sumCalories = 0
    for line in f:
        if not line.strip():
            heapq.heappush(heap, -sumCalories)
            sumCalories = 0
        else:
            sumCalories += int(line)
    heapq.heappush(heap, -sumCalories)

print("Part 1: ", -heap[0])
print("Part 2: ", calc_n_max(3))