# Everything is in order

import numpy as np

def sort_columns(matrix):

    sorted_matrix = np.sort(random_matrix, axis=0)
    return sorted_matrix

#set random seed to generate matrix
np.random.seed(12345)
random_matrix = np.random.randint(1, 50, (4, 5))

# Test Case
print('Original Matrix')
print(random_matrix)


print('Sorted Matrix')
sorted_matrix = sort_columns(random_matrix)
print(sorted_matrix)

'''Output
Original Matrix
[[35 38 30  2 37]
 [42 38 35 30  2]
 [15 42 28 17 10]
 [12 14 11 18 19]]
Sorted Matrix
[[12 14 11  2  2]
 [15 38 28 17 10]
 [35 38 30 18 19]
 [42 42 35 30 37]]
'''