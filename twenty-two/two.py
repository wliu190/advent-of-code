import numpy as np
'''
Day 2: Rock Paper Scissors
Rock: A/X
Paper: B/Y
Scissors: C/Z

1 for Rock, 2 for Paper, 3 for Scissors
0 for losing, 3 for drawing, 6 for winning

What would the score be if I followed the strategy guide?
'''

score1_m = np.array([[4,8,3],[1,5,9],[7,2,6]])
score2_m = np.array([[3,4,8],[1,5,9],[2,6,7]])

def scorer(x):
    ''' 
    A function that returns points for a given round
    Input: ['opponent' 'me']
    '''
    opp = 'ABC'.index(x[0])
    me = 'XYZ'.index(x[2])
    #score = score1_m[opp,me] # for part 1
    score = score2_m[opp,me] # for part 2
    return score


with open('data/two.txt') as f:
    lines = f.readlines()
    rounds = [line.strip() for line in lines]
    scores = [int(scorer(x)) for x in rounds]

print(np.sum(scores))