tasks=[]
while True:
    task=input('do you want to add, remove, update an task or print the tasks ')
    if task=='add':
        task_add=input('what task do you want to add? ')
        tasks.append(task_add)
    elif task=='remove':
        task_rem=input('what task do you want to remove? ')
        tasks.remove(task_rem)
    elif task=='update':
        task_updt=input('what task do you want to update? ')

