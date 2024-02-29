# List Slicing and Striding

#2.1 

num_list = []
for i in range(51):
    num_list = num_list + [i]
print(num_list)

'''
Test Case Output: 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

An error I came across was:
"TypeError: can only concatenate list (not "int") to list"
I fixed it by putting brackets around i after the plus sign
'''


#2.2

def square_func(numbers):
    squared_numbers = []
    for num in numbers:
        squared_numbers.append(num ** 2)
    return squared_numbers

'''
Test Case:
original_numbers = [1, 2, 3, 4, 5]
squared_numbers = square_func(original_numbers)
print(squared_numbers)

Output: [1, 4, 9, 16, 25]
'''

#2.3

def odd_func(listA, listB):

    
    combined_list = listA + listB
    list_odd = []

    for num in combined_list:
        if num % 2 != 0:
            list_odd.append(num)

    sorted_odd_list = sorted(list_odd)
    return sorted_odd_list


'''
Test Case:
listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listB = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

print(odd_func(listA, listB))

Ouput:[1, 3, 5, 7, 9, 21, 23, 25, 27, 29]

An error I came across was:
 when I ran the code, the output was "None"
 I fixed this by adding return sorted_odd_list, as I had forgotten to add that
 so when I called the function, nothing was returned

'''
