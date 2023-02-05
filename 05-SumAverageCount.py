# -------------------------------------
# Part I -  Calc sum of of a given list
# -------------------------------------

count = 0
sum = 0
print (f'''
Before loop start 'Count' = {count} / 'Sum' = {sum}
---------------------------------------------------
''')
for num in [1, 14,32, 2, -2, 4, -12, 23] :
    count += 1
    sum = sum + num
    print(f'Count: {count} // Sum = {sum}')
average = sum/count
print(f'''
----------------
After the loop :
Count   = {count} 
Sum     = {sum}
Average = {average}
-----------------
''')

# ------------------------------
# Part 2 - Calcuate sum till 'n'
# ------------------------------

nval = int(input('Please type an "n" value: '))
sum2 = 0
for num in range(0, nval+1) :
    sum2 = sum2 + num
print(f'Sum of numbers from 0 to "n" is: {sum2}')