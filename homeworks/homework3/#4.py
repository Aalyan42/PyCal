#4

def bmi(weight, height):

    #BMI formula is kg/m^2
    return (weight / (height ** 2))


'''
TEST CASE:

weight = 70
height = 2
print(bmi(weight, height))

Output was 17.5
'''