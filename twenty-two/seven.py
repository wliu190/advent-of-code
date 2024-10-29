import numpy as np
import re

"""
Day 7: No Space Left on Device
Elves are still having problems with their comms devices: they're running out of space!
Go through all the device directories and find all directories with a total size of at most 100,000.
What is the sum of the total sizes of these directories?
"""

# list of directory sizes as integers (call them tallies)
# every time we do cd x, add a new tally (initialise as zero)
# every time we do ls, move forward index, add any data to the tally and to all parent directories
# every time we do cd .., move back index (keep a counter)

def form_directories():
    with open('data/seven.txt') as f:
        lines = f.read().splitlines()
        dir_sizes = []
        index = [] # records the 'path' 
        tally = 0 # records how many directories we have 
        for line in lines:
            if line.split()[1] == 'cd':
                if line.split()[2] != '..':
                    dir_sizes.append(0)
                    index.append(tally)
                    tally += 1
                else:
                    # move back to parent by erasing path 
                    index.pop()
            elif (line.split()[0] != 'dir') and (line.split()[1] != 'ls'):
                # add file size to current path
                for i in index:
                    dir_sizes[i] += int(line.split()[0])

        return dir_sizes
    
def analyse_dir(dir_sizes):
    """analyse directory sizes to help the Elves"""
    at_most = [size for size in dir_sizes if size <= 100000]
    free_smallest = min([size for size in dir_sizes if size >= 8381165])

    return at_most, free_smallest

dir_sizes = form_directories()
at_most, free_smallest = analyse_dir(dir_sizes)
print(free_smallest)