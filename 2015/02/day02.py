# https://adventofcode.com/2015/day/2

import numpy as np

with open("input.txt") as f:
    lines = [line.rstrip().split('x') for line in f]
    dims = np.array(lines, dtype=int)   # [l, w, h]
    # Part 1:
    sides = np.array([dims[:,0]*dims[:,1], dims[:,1]*dims[:,2], dims[:,0]*dims[:,2]]).T  # [l*w, w*h, l*h]
    minSide = np.min(sides, axis=1)
    wrapPerGift = 2 * np.sum(sides, axis=1) + minSide
    print("Part 1:", np.sum(wrapPerGift))
    # Part 1:
    maxDim = np.max(dims, axis=1)
    ribbonPerGift = 2 * (np.sum(dims, axis=1) - maxDim)
    bowPerGift = np.prod(dims, axis=1)
    ribbon = np.sum(ribbonPerGift) + np.sum(bowPerGift)
    print("Part 2:", ribbon)