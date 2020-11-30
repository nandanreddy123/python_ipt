try:
    print(error)
except NameError as ne:
    print(ne)
except :
    print('your code has errors')