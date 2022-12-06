"""
https://adventofcode.com/2022/day/5
Advent of Code 2022 - Day 5
--- Supply Stacks ---

Program Logic:
- initializeStacks() initializes the stacks as a list of strings.
  e.g.      [D]    
        [N] [C]       ->  ['ZN', 'MCD', 'P']
        [Z] [M] [P]

- moveCrates() makes the moves, based on the part
  e.g. for the above example and the instruction 'move 2 from 2 to 3'
    part A: 2 'M' <- 'MCD' , 'PDC' <- 'P' + 'CD'[::-1]  => ['ZN', 'M', 'PDC']
    part B: 2 'M' <- 'MCD' , 'PCD' <- 'P' + 'CD'        => ['ZN', 'M', 'PCD']

The most difficult part was parsing the data
"""
from parse import parse

def initializeStacks(crates):
  num_stacks = (len(crates[0])+1)//4
  stacks = [""] * num_stacks
  for line in crates[-2::-1]:
    for i in range(1, len(line), 4):
      stacks[i//4] += line[i] if line[i] != ' ' else ''
  return stacks

def moveCrates(stacks, moves, partB):
  stacks = stacks.copy()
  for move in moves:
    num_items, source, destination = parse("move {:d} from {:d} to {:d}", move)
    moved = stacks[source-1][-num_items:] if partB else stacks[source-1][-1:-1-num_items:-1]
    stacks[destination-1] += moved
    stacks[source-1] = stacks[source-1][:-num_items]
  return ''.join([stack[-1] for stack in stacks])


def main():
  with open("in.txt") as f:
    lines = f.read()
  crates, moves = [part.split('\n') for part in lines.split('\n\n')]
  stacks = initializeStacks(crates)
  print(stacks)
  print("Part 1: ", moveCrates(stacks, moves, False))
  print("Part 2: ", moveCrates(stacks, moves, True))

if __name__ == "__main__":
  main()