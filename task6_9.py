num1=int(input('enter the first value'))
num2=int(input('enter the second value'))
action= input('press corresponding symbols for calculation')

if(action == '+'):
    print('addition of',num1,',',num2,'is',num1+num2)
elif(action == '-'):
    print('subtraction of',num1,',',num2,'is',num1-num2)
elif(action == '/'):
    print('division of',num1,',',num2,'is',num1/num2)
elif(action == '*'):
    print('multiplication of',num1,'and',num2,'is',num1*num2)