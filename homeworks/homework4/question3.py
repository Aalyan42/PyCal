#3.1

count = 1
two_d_list = []

for i in range(5):
    row = []
    for j in range(5):
        row.append(count)
        count += 1 
    two_d_list.append(row)

for row in two_d_list:
    print(row)


'''
Test Case Output: 
[1, 2, 3, 4, 5]
[6, 7, 8, 9, 10]
[11, 12, 13, 14, 15]
[16, 17, 18, 19, 20]
[21, 22, 23, 24, 25]

Error came across was outputted all numbers in each row, so row 2 was 1-10 and row 5 was 1-25.
Fixed by changing code to add a count, and stored the lists in two_d_list. The reason I now get five rows of five numbers
instead of one long row of 25 numbers is because the nested for loop structure creates a separate row list for each iteration
of the outer loop and appends each row to two_d_list.


'''



#3.2

count = 1
two_d_list = []

for i in range(5):
    row = []
    for j in range(5):
        if count % 3 == 0: 
            row.append('?')
        else:
            row.append(count)
        count += 1
    two_d_list.append(row)

for row in two_d_list:
    print(row)



'''
Test Case Output: 
[1, 2, '?', 4, 5]
['?', 7, 8, '?', 10]
[11, '?', 13, 14, '?']
[16, 17, '?', 19, 20]
['?', 22, 23, '?', 25]
'''