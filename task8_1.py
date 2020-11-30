#two types of errors syntax and logic
try:
    a=1/0
#zero division error is logic
except ZeroDivisionError as zd:
    print('the error of given programme is',zd)
#syntaxerror
except SyntaxError as se:
    print('the error is ',se)