import re
string= 'the numbers i like are 2,14,22,234'
search= re.finditer(r'([0-9]{1,3})',string)
lists = []
for i in search:
    lists.append(i)
print(len(lists))