import numpy as np

"""
Day 8: Tree House
The Elves are trying to find an ideal tree to build a tree house.
They want a tree where there is a direct line to the edge with shorter trees, this would make it invisible. 
How many trees are visible from outside the grid?
"""
def incorrect_find_visible_trees():
    with open('data/test.txt') as f:
        height_array = np.array([[int(x) for x in line.strip()] for line in f])
        length, width = height_array.shape[0], height_array.shape[1]
        n, e, s, w = [[(0,i) for i in range(width)]], [[(i,width-1) for i in range(width)]], \
                                [[(length-1,i) for i in range(width)]], [[(i,0) for i in range(width)]]  
        visible_trees = set(n[0]) | set(e[0]) | set(s[0]) | set(w[0])

        while (len(n[-1]) != 0) and (len(e[-1]) != 0) and (len(s[-1]) != 0) and (len(w[-1]) != 0):
            n_new = [(idx[0]+1,idx[1]) for idx in n[-1] if (height_array[idx[0]+1,idx[1]]) > (height_array[idx[0],idx[1]])]
            e_new = [(idx[0],idx[1]-1) for idx in e[-1] if (height_array[idx[0],idx[1]-1]) > (height_array[idx[0],idx[1]])]
            s_new = [(idx[0]-1,idx[1]) for idx in s[-1] if (height_array[idx[0]-1,idx[1]]) > (height_array[idx[0],idx[1]])]
            w_new = [(idx[0],idx[1]+1) for idx in w[-1] if (height_array[idx[0],idx[1]+1]) > (height_array[idx[0],idx[1]])]

            visible_trees = visible_trees.union(set(n_new), set(e_new), set(s_new), set(w_new))
            n.append(n_new), e.append(e_new), s.append(s_new), w.append(w_new)

            print('e: ',e)
            print('len: ',len(e[-1]))
            print('e[-1]: ', e[-1])
        return visible_trees


def clear_search(idx, height_array):
    """
    Input: idx in the form [i,j]
    Output: idx of visible trees
    """
    height = height_array[idx[0], idx[1]]
    north = height_array[:idx[0],idx[1]]        
    south = height_array[idx[0]+1:,idx[1]]        
    east = height_array[idx[0],idx[1]+1:]
    west = height_array[idx[0],:idx[1]]
    if all(i < height for i in north) or  all(i < height for i in south) or  all(i < height for i in east) or  all(i < height for i in west):
        return True

def find_visible_trees():
    """
    Correct function for Part I
    """
    with open('data/eight.txt') as f:
            height_array = np.array([[int(x) for x in line.strip()] for line in f])
            length, width = height_array.shape[0], height_array.shape[1]
            border_trees = 2*length+2*width-4
            clear_trees = 0
            # scan interior trees
            for i in range(1,width-1):
                for j in range(1,width-1):
                    if clear_search([i,j], height_array) == True:
                        clear_trees += 1

            print(clear_trees+border_trees)
                  
# Part II: Scoring #
####################


def scenic_scorer(height, vector):
    """
    Figures out the score 
    """
    score = 0
    # edge
    if len(vector) == 0: # edge case
        score += 0
    elif all(i < height for i in vector): # case where there is no higher tree
        score += len(vector)
    else: # find the first tree that blocks the view
        idx = np.where(height <= vector)[0][0]
        score = idx + 1
    print("height: ", height, "vector: ", vector, "score: ", score)
    return score

def scenic_search(idx, height_array):
    """
    Function for searching 
    """
    height = height_array[idx[0], idx[1]]
    north = np.flip(height_array[:idx[0],idx[1]])
    south = height_array[idx[0]+1:,idx[1]]        
    east = height_array[idx[0],idx[1]+1:]
    west = np.flip(height_array[idx[0],:idx[1]])

    scenic_score = 1

    for direction in north, south, east, west:
        score = scenic_scorer(height, direction)
        scenic_score *= score
    print(scenic_score)
    return int(scenic_score)

def max_scenic_score():
    """
    Does the actual problem
    """
    with open('data/eight.txt') as f:
            height_array = np.array([[int(x) for x in line.strip()] for line in f])
            length, width = height_array.shape[0], height_array.shape[1]
            scores = []
            for i in range(0,width):
                 for j in range(0, width):
                      scores.append(scenic_search([i,j], height_array))
            return scores

scores = max_scenic_score()
print(max(scores))