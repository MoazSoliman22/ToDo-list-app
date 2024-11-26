import json
import os

FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = rf'{FOLDER_PATH}\todo_list.json'


with open(FILE_PATH,"r") as f:
    try:
        tasks = json.load(f)
    except json.JSONDecodeError:
        tasks = []

def save_tasks():
    with open(FILE_PATH,'w') as f:
        json.dump(tasks,f,indent=4)

def view_tasks():
    if len(tasks) == 0:
        print("You don't have any tasks")
        return False
    else:
        print('-'*25,'Tasks','-'*25)
        for label , task in enumerate(tasks,1):
            print(f"{label}. {task['task name']} {['completed' if task['completed'] == True
                                            else 'not completed']}")
        print('\n')

def add_task():
    task = input("Enter a task: ")
    tasks.append({'task name' : task,'completed' : False})
    save_tasks()
    print('\nTask added ✅')

def mark_task():
    if len(tasks) == 0:
        print("You don't have tasks to mark")
    else:
        view_tasks()
        try:
            task_number = int(input('Enter task number: ')) - 1
            if  0 <= task_number < len(tasks):
                if tasks[task_number]['completed'] == False:
                    tasks[task_number]['completed'] = True
                else:
                    tasks[task_number]['completed'] = False
                print('Task marked ✅')
                save_tasks()
            else:
                print('Invalid task number')
        except ValueError:
            print('Invalid input')

def delete_task():
    if len(tasks) == 0:
        print('You don\'t have tasks to remove')
    else:
        view_tasks()
        try:
            task_number = int(input('Enter task number: ')) - 1
            if 0 <= task_number < len(tasks):
                tasks.pop(task_number)
                print('Task deleted ✅')
                save_tasks()
            else:
                print('Invalid task number')
        except ValueError:
            print('Invalid input')

def main():
    while True:
        print("Options:"
            "\n1. Add a task"
            "\n2. Mark as done"
            "\n3. Delete a task"
            "\n4. View tasks"
            "\n5. Exit\n")
        choice = input("Make a decision (1-5): ")
        while choice not in ['1','2','3','4','5']:
            choice = (input("Make a decision (1-5): "))

        if choice == '1':
            add_task()
        elif choice == '2':
            mark_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            view_tasks()
        elif choice == '5':
            break
main()
