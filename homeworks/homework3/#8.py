#8

def digital_root(int):

    digits_sum = 0

    while int > 0:
        #add last digital to digit_sum
        digits_sum += int % 10
        #remove the last digit
        int = int // 10

    return digits_sum
    
'''
sample_num = 12345
print(digital_root(sample_num))
Output is 15
'''