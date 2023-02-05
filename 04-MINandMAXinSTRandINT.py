# In Python, when looking into MIN andMAX values for STR, in ranking CAPITAL letters 
# come before small captioned letters => small letters have HIGHER ranking!!!

varint = [1, 4, -5, 16, -89, 398]
varstr1 = "Hello world"
varstr2 = "Hello World"
varintmin = min(varint)
varintmax = max(varint)
varstr1min = min(varstr1)
varstr1max = max(varstr1)
varstr2min = min(varstr2)
varstr2max = max(varstr2)

print (f'''
Int list is       : {varint}
min number        = {varintmin}
max number        = {varintmax}
*************************
Str No.1 is       : {varstr1}
Smallest letter is: {varstr1min}
Biggest letter is : {varstr1max}
{'*'*25}
Str No.2 is       : {varstr2}
Smallest letter is: {varstr2min}
Biggest letter is : {varstr2max}
''')