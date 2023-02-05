largest = None
print('Before Loop')
for value in [-3, 3,14,-10, 98, 23, 1, 0, 16] :
    if largest == None:
        largest = value
    elif value > largest : 
        largest = value
    print('Largest so far =', largest)
print('After Loop')
print ('Final largest =', largest)

largest2:int = None
print('*'*10)
print('2nd pass - start of loop')
for value in [-3, 3,14,-10, 98, 23, 1, 0, 16] :
    if largest2 == None :
        largest2 = value
    elif largest2 < value : 
        largest2 = value
    print('Largest2 so far is:', largest2)
print('end of loop 2')
print('Largest 2 in this loop is:',largest2)