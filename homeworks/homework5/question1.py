#Hey Twin

import numpy as np

def findEquals(arr):
    equal_rows = []

    for row in arr:
        # Check if all elements in the current row are equal to the first element
        if np.all(row==row[0]):
            equal_rows.append(row)
        
    return np.array(equal_rows)
    

#Test Case

arr = np.array([[1, 1, 1], [1, 2, 3], [2, 2, 2]])

print(findEquals(arr))

'''Output
[[1 1 1]
 [2 2 2]]
 '''