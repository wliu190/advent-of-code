import numpy as np
import re
'''
Day 4: Supply Stacks
Supplies are stored in stacks of crates. The Elves are trying to figure out which crate will end up where.
We have both the initial arrangement, and the series of moves that the crane operator will move.

After the rearrangement procedure, what crate ends up on top of each stack?
'''
def import_data():
    with open('data/five.txt') as f:
        lines = f.read().splitlines()
        initial_config = lines[:lines.index('')]
        stack_num = len(initial_config[-1].split())
        stacks = []

        # arrange by stacks #
        #####################
        for j in range(stack_num):
            stack = []
            for i in initial_config[:-1]:
                crate = i[4*j+1]
                if crate != ' ':   
                    stack.append(crate)
            stacks.append(stack)

        moves_data = lines[lines.index('')+1:]
        moves = [[int(i) for i in re.findall(r'\d+', line)] for line in moves_data]

    return stacks, moves


def move_crates_9000(data, start, end, quantity):
    for i in range(quantity):
        data[end].insert(0, data[start][0])
        data[start].pop(0)

def move_crates_9001(data, start, end, quantity):
    for i in range(quantity):
        data[end].insert(0, data[start][quantity-i-1])
        data[start].pop(quantity-i-1)

def unload_crates():
    stacks, moves = import_data()
    for i in range(len(moves)):
        move_crates_9001(stacks, moves[i][1]-1, moves[i][2]-1, moves[i][0])
    return stacks

final_stacks = unload_crates()

print(final_stacks)
for i in range(9):
    print(final_stacks[i][0])