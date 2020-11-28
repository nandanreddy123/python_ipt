looplist= [1,2,3,4,5,6]
for i in looplist:
    x = i+2
    looplist.append(x)
    looplist.remove(i)
print(looplist)