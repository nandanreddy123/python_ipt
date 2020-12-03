numbers_list = [3, 4, 2, 5, 6, 7, 9, 23, 22, 14]
odd_list = []


def logic(i):
    if i % 2 == 0:
        return False
    else:
        return True


filter_list = filter(logic,numbers_list)
for number in filter_list:
    odd_list.append(number)
print(odd_list)
