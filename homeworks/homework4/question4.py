
def remove_duplicates(list):
    final_list = []
    for num in list:
        if num not in final_list:
            final_list.append(num)
    return final_list

list = [1, 1, 2, 3, 4, 4]

print(remove_duplicates(list))


'''
Test Case Outpute: [1, 2, 3, 4]
'''