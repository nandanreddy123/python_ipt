fibonacci = [0,1]
x = 0
y = 1
for i in range(1,100):
    z = x + y
    x = y
    y = z
    fibonacci.append(z)
print('the fibonacci sequence from 1 to 100',fibonacci)