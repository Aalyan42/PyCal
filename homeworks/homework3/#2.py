#2

def min_max(numbers):

    #assign the minimum and maximum values with a starting point
    min_val = numbers[0]
    max_val = numbers[0]

    #go through list and find minimum and maximum values 
    for num in numbers[0:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return (min_val, max_val)

'''
TEST CASE:

num_list = [1,2,3,4,5,6]

#calls min_max function with num_list, and returns a tuple
minmax_output = min_max(num_list)

print(minmax_output)

Output was (1, 6)
'''