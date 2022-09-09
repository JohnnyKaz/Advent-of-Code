"""
https://adventofcode.com/2015/day/9
Advent of Code 2015 - Day 9
--- All in a Single Night ---
"""

import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations

def drawGraph(G):
    pos=nx.spring_layout(G)
    nx.draw(G,pos, with_labels=True)
    edge_labels = dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    plt.show()
    
def solve(G, reverse=False):
    perms = permutations(G.nodes)
    weights = [nx.path_weight(G, p, 'weight') for p in perms]
    return max(weights) if reverse else min(weights)

with open('input.txt', 'r') as f:
    G = nx.Graph()
    for line in f:
        param = line.strip().split(' ')
        G.add_edge(param[0], param[2], weight=int(param[-1]))
    print("Part 1:", solve(G))
    print("Part 2:", solve(G, True))
    drawGraph(G)
