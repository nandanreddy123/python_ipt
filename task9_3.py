given_number = int(input("enter the number to multiply by"))
given_list = [4,5,3,7,8]
multiply_list = []
for i in given_list:
    expression = lambda i,gn : i*given_number
    multiply_list.append(expression(i,given_number))
print(multiply_list)