#3

def leap_year(year):

    if year % 4 != 0:
        return False
     
    elif year % 100 == 0 and year % 400 != 0:
        return False
    
    else:
        return True

'''
Had this before, but other seemed more efficient:

    if year % 400 == 0:
        return True
    
    elif year % 100 ==0:
        return False

'''



'''
TEST CASE:

year = 2000
print(leap_year(year))
    Output was True

year = 2003
print(leap_year(year))
    Output was False

'''

