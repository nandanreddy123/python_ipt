def task_insert(task):
     x= int(input("enter the number to insert into task list"))
     task.append(x)
     print (task)
     return


def task_delete(task):
    x= int(input("enter the number to delete in the list"))
    task.remove(x)
    print(task)
    return

task =[4,5,6,7,8,9]
task_insert(task)
task_delete(task)
minmum=min(task)
maximum=max(task)