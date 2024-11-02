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
    knot_coords = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0], [0,0]]

    for move in moves:
        print("#### MOVE!: ",move, '####')
        for i in range(move[1]):
            print("step: ", i)
            knot_coords = knot_move(knot_coords, move_dict[move[0]])
            t_pos.add(tuple(knot_coords[-1]))
    
    return t_pos

def knot_move(knot_coords, move):
    lead_old = knot_coords[0]
    move_old = [0,0]
    knot_coords[0] = [sum(x) for x in zip(knot_coords[0], move)]
    
    for i in range(len(knot_coords)-1):
        print('new loop')
        print("old move", move_old, "lead_old: ", lead_old)
        lead_new, chase_new = make_move(move_old, lead_old, knot_coords[i], knot_coords[i+1])
        move_old = [x[1] - x[0] for x in zip(knot_coords[i+1],chase_new)]
        lead_old = knot_coords[i+1]
        knot_coords[i] = lead_new
        knot_coords[i+1] = chase_new
        print(knot_coords, "new lead and chase", lead_new, chase_new)    
    return knot_coords

def make_move(move_old, lead_old, lead_new, chase_coord):
    """
    Given the positions of lead (H) (after move) and chase (T) and the individual move,
    return the new coordinate of both at the end of the moves
    """
    # three cases: (1) H is on top, (2) H is adjacent, (3) H is diagonal 
    # (1): for all H moves, do nothing
    # (2): if H moves along line H-T, then move to old H, otherwise do nothing
    # (3): if H moves away from T, move to old H, otherwise do nothing
    # but in part II, now the "lead" can move diagonally
    # if the lead piece doesn't move diagonally, follow old rules
    # if the lead piece does move diagonally, then all following pieces move in the same way

    if dist(lead_new, chase_coord) == 2:
        # make the move that steps towards lead knot
        print(lead_new, chase_coord)
        for x in ([1,0], [-1,0], [0,1], [0,-1]):
            test_move = [sum(a) for a in zip(chase_coord, x)]
            if dist(lead_new, test_move) == 1:
                print("x ", test_move)
                chase_new = test_move 

    elif dist(lead_new, chase_coord) > np.sqrt(2):
        if np.sqrt(np.square(move_old[0])+np.square(move_old[1])) == np.sqrt(2): 
            chase_new = [sum(x) for x in zip(chase_coord, move_old)]
        else:
            chase_new = lead_old
    else:
            chase_new = chase_coord

    return lead_new, chase_new

def dist(h_coord, t_coord):
    return np.sqrt(np.square(h_coord[0]-t_coord[0]) + np.square(h_coord[1]-t_coord[1]))


print(len((rope_mover()))-1)