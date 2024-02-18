#1

def num_power(x,y):

    #case when y = 0
    if y == 0:
        return 1
    result = 1

    #case when y > 0
    if y < 0:
        x = 1 / x
        y = -y

    # multiply x by itself, y times
    # I am using _ to indicate that the loop variable is not being used in the loop
    for _ in range(y):
        result *= x

    return result

'''
TEST CASE:
print (num_power(5,2))
result was 25

print (num_power(6,0))
result was 1

print (num_power(5,-2))
result was 0.04 (which is 1/25)
'''