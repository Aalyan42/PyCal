#Checkers

import numpy as np

def checkerboard():
    board = np.zeros((8, 8), dtype=int)

    board[1::2, 2] = 1
    board[::2, 1::2] =1

    return board

#Test 
pattern = checkerboard()
print(pattern)

'''Output
[[0 1 0 1 0 1 0 1]
 [0 0 1 0 0 0 0 0]
 [0 1 0 1 0 1 0 1]
 [0 0 1 0 0 0 0 0]
 [0 1 0 1 0 1 0 1]
 [0 0 1 0 0 0 0 0]
 [0 1 0 1 0 1 0 1]
 [0 0 1 0 0 0 0 0]]
 '''