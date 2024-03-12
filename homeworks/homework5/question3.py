# I need some space

import numpy as np

def wordSpacer(arr):

    spaced_wordlst = []
    
    for string in arr:
        characters = list(string)
        spaced_word = ' '.join(characters)
        spaced_wordlst.append(spaced_word)
    #converting list of strings to NumPy array, defining the data type of the array's elements
    return np.array(spaced_wordlst, dtype='<U11')

#Test Case

arr = np.array(['python', 'is', 'cool'])
spaced_arr = wordSpacer(arr)
print(spaced_arr)

'''Output
['p y t h o n' 'i s' 'c o o l']
'''