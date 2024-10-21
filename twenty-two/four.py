import numpy as np
'''
Day 4: Camp Cleanup
The elves are paired up to clean up parts of the camp, where each section is numbered.
We want to find the assignments where one elf's assignment fully contains the other.
'''

with open('data/four.txt') as f:
    lines = f.read().split('\n')
    assignments = [[[int(y) for y in x.split('-')] for x in line.split(',')] for line in lines]
    ranges = [np.arange(assignment[0][0],assignment[0][1]+1) for assignment in assignments]

    entire_overlaps, overlaps = 0,0
    for x in assignments:
        a1,a2 = np.arange(x[0][0],x[0][1]+1), np.arange(x[1][0],x[1][1]+1) 
        entire_overlaps += np.intersect1d(a1,a2).size == np.min([a1.size,a2.size]) # check if intersection of ranges is an entire range
        overlaps += np.intersect1d(a1,a2).size > 0

print(entire_overlaps)
print(overlaps)