import re
task_list=['azaz','amar','0829','0456','AmaZ']
pattern="[a-zA-Z0-9]"
for i in task_list:
    print(re.findall(pattern,i))