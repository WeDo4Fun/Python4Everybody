# -------------------------------------------------------
# Example for Boolean Variable to find a variable in list
# -------------------------------------------------------

found = False
# foundtype = type(found)
# print(f'Type for "found" variable in code is: {foundtype}")
print('Start of Loop')
print('-------------')

count = 0

for value in (9, 41, 12, 3, 74, 58, 33) : 
    if value == 3 :
        found = True
        count =+ 1
    print (f'Value = {value} : Boolean = {found}')
    found = False