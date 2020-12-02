import re
string='nandan12'
pattern = '[0-9$]'
print(re.findall(pattern,string))