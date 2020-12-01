task_list = [27,19,16,18,24]
divisible_list = []
for i in task_list:
    if (i%9) == 0 :
        divisible_list.append(i)
print(divisible_list)