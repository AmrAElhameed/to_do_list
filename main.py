from art import logo
import clear
def add_task():
    """Adding a task to the tasks list with a default status as uncompleted"""
    task = {'task': input('please add a task:\n'), 'status': 'uncompleted'}
    tasks.append(task)
    print('your task was added successfully')

def view_tasks():
    """View all the tasks you have inserted"""
    for i in range(len(tasks)):
        print(f'{i + 1}- {tasks[i]}')

def mark_task_as_completed():
    """Mark the task you choose as completed"""
    i = 0
    task = {}
    for task in tasks:
        if task['status'] == 'uncompleted':
            print(f'{i + 1}- {tasks[i]}')
        i += 1
    while task['status'] == 'uncompleted':
        index = int(input('please select the task you want to mark as completed:\n'))
        tasks[index - 1]['status'] = 'completed'
        print("you have successfully marked your task as completed ")
        break
    if task['status'] != 'uncompleted':
        print('you dont have any pending tasks')

def edit_task():
    """Edit the task you choose by removing or editing the main task or the task status."""
    view_tasks()
    nu = int(input('choose which task you want to edit from the list above:\n'))
    nu_index = nu - 1
    action = input('to remove the task Enter "1", to edit the task Enter "2":\n')
    if action == "1":
        tasks.remove(tasks[nu_index])
        print(f'The Task number({nu})has been deleted.')
    elif action == "2":
        edit_type = input(
            'for editing task Enter "1", To change Task Status from completed to uncompleted Enter "2":\n')
        if edit_type == "1":
            print(tasks[nu_index])
            tasks[nu_index]['task'] = input('please Enter the task you want to replace with the one above:\n')
            print('your task was replaced successfully.')
        elif edit_type == "2":
            print(f'the task to edit the status for is: {nu}-{tasks[nu_index]}')
            tasks[nu_index]['status'] = 'uncompleted'
            print('your task status was updated successfully')

to_do = True
tasks = []

def to_do_list():
    global to_do
    print(logo)
    while to_do:
        print('''
        1- add a task.
        2- view tasks.
        3- mark tasks as completed.
        4- edit tasks.
        5- Quit.
        ''')
        choice = int(input('please select from the list above:\n'))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            mark_task_as_completed()
        elif choice == 4:
            edit_task()
        elif choice == 5:
            print('thanks for using "todolist".')
            to_do = False
        else:
            print('you entered an invalid information.\nplease try again.')

clear.clear()
to_do_list()