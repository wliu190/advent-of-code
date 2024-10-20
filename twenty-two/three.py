import numpy as np
'''
Day 3: Rucksack reorganisation
Each rucksack has two compartments. We need to sort items into the compartments (always equally divided)
Each item is identified by a letter (case-sensitive). 
We need to find an error in packing, where items have been placed in both compartments.
Each item has a priority to help us decide where to start.

What is the sum of the priorities of the items that have been duplicated?

Part 2 
The Elves are in groups of 3, each carrying the same item. 
'''

priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def match_finder(x):
    half_length = int(len(x)/2)
    return set(x[:half_length]) & set(x[half_length:])

with open('data/three.txt') as f:
    lines = f.read().split('\n')
    matches_1 = [match_finder(line) for line in lines]
    priorities_1 = [[priority.index(x)+1 for x in a] for a in matches_1]

    matches_2 = [set(lines[i]) & set(lines[i+1]) & set(lines[i+2]) for i in range(0, len(lines), 3)]
    priorities_2 = [[priority.index(x)+1 for x in a] for a in matches_2]
    
#print(np.sum(priorities_1))
print(np.sum(priorities_2))