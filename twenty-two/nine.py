import numpy as np
import re

"""
Day 9: Rope Bridge
An old rope bridge has a knot at each end marking the 'head' and 'tail' of the rope,
which we can model as a 2D grid.
If the head moves far enough away form the tail, the tail is pulled towards the head.
The head (H) and tail (T) must be always be touching (diagonal included) or overlapping.

The tail moves up/down/left/right if the head is directly two steps away.
The tail moves diagonally if the head and tail aren't in the same row/column.
"""
def rope_mover():
    move_dict = {
        "R": [1,0],
        "U": [0,1],
        "L": [-1,0],
        "D": [0,-1]
    }

    with open('data/nine.txt') as f:
        # import data
        lines = f.read().splitlines()
        moves = [(line[0],int(re.findall(r'[0-9]+', line)[0])) for line in lines]

    t_pos = set((0,0))
    h_coord, t_coord = [0,0], [0,0]

    for move in moves:
        for i in range(move[1]):
            h_coord, t_coord = make_move(h_coord, t_coord, move_dict[move[0]])
            t_pos.add(tuple(t_coord))
    return t_pos

def make_move(lead_coord, chase_coord, move):
    """
    Given the positions of lead (H) and chase (T) and the individual move,
    return the new coordinate of t at the end of the moves
    """
    # three cases: (1) H is on top, (2) H is adjacent, (3) H is diagonal 
    # (1): for all H moves, do nothing
    # (2): if H moves along line H-T, then move to old H, otherwise do nothing
    # (3): if H moves away from T, move to old H, otherwise do nothing
    lead_new = [sum(x) for x in zip(lead_coord, move)]

    if dist(lead_new, chase_coord) > np.sqrt(2):
        chase_new = lead_coord
    else: 
        chase_new = chase_coord
    return lead_new, chase_new

def dist(h_coord, t_coord):
    return np.sqrt(np.square(h_coord[0]-t_coord[0]) + np.square(h_coord[1]-t_coord[1]))


print(len((rope_mover()))-1)