#5

def rotate_digits(n):

    last_digit = n % 10

    rest_numbers = n // 10

    #use a multiplier to find where the last digit has to be placed after rotation, count digits in rest_numbers to find multiplier
    temp = rest_numbers
    multiplier = 1
    while temp > 0:
        multiplier *= 10
        temp //= 10
    
    rotated_number = last_digit * multiplier + rest_numbers
    return rotated_number


'''
TEST CASE:

print(rotate_digits(12345))
Output was 51234

print(rotate_digits(56789))
Output was 95678

'''