import re
string='NANDA'
pattern ='[A-Z]'
search=re.findall(pattern,string)
if len(search) < len(string):
    print('invalid input')
else:
    print('valid input')