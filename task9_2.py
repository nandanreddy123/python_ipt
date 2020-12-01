limit = int(input('enter the limit of fibonacci series'))
fibonacci_list = [0,1]
first = 0
second = 1
while len(fibonacci_list) < limit:
        expression = lambda fi,se:first+second
        append = expression(first, second)
        fibonacci_list.append(append)
        first = second
        second = append
print(fibonacci_list)