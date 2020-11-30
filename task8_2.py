try:
    a= int(input('enter the value of a'))
    b= int(input('enter the value of b'))
    def add(a,b):
        print('the addition of given two numbers is',a+b)
    def sub(a,b):
        print('the substraction of two given numbers is',a-b)
    def div(a,b):
        print('the division of given two numbers is',a/b)
    def multi(a,b):
        print('the multiplication of two given numbers is',a*b)
    process=input('enter the application to perform +,-,*,/  \n')
    if(process == '+'):
        add(a,b)
    elif(process =='-'):
        sub(a,b)
    elif(process == '*'):
        multi(a,b)
    elif(process == '/'):
        div(a,b)
    else:
        print('invalid process input')
except ZeroDivisionError :
    print('the value of b cannot be zero')