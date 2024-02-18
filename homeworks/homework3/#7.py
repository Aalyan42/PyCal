#7

def vowel_count(string):

    vowels = 'aeiouAEIOU'

    vowel_count = 0

    for char in string:
        if char in vowels:
            vowel_count += 1

    return(vowel_count)

'''
sample_string = "Python Decal"
print(vowel_count(sample_string))

Output: 3
'''