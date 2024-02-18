#6

def min_for(arr):

    #assign the minimum value with a starting point like before
    min_val = arr[0]

    for num in arr:
        if num < min_val:
            min_val = num

    return min_val

'''
TEST CASE:

num_list = [1,2,3,4,5,6]

min_output = min_for(num_list)

print(min_output)

Outputs 1
'''

def max_for(arr):

    max_val = arr[0]
    
    for num in arr:
        if num > max_val:
            max_val = num

    return max_val    

'''
TEST CASE:

num_list = [1,2,3,4,5,6]

max_output = max_for(num_list)

print(max_output)

Outputs 6
'''

def min_while(arr):

    min_val = arr[0]

    i = 1
    while i < len(arr):
        if arr[i] < min_val:
            min_val = arr[i]
        i += 1

    return min_val

'''
TEST CASE:

num_list = [1,2,3,4,5,6]

min_output = min_while(num_list)

print(min_output)

Output is 1
'''

def max_while(arr):

    max_val = arr[0]

    i = 1
    while i < len(arr):
        if arr[i] > max_val:
            max_val = arr[i]
        i += 1
        
    return max_val

'''
TEST CASE:

num_list = [1,2,3,4,5,6]

max_output = max_while(num_list)

print(max_output)

Output is 1
'''