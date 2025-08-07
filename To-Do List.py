tasks = []

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['completed']}\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task, completed = line.strip().split("|")
                tasks.append({'task': task, 'completed': completed == 'True'})
    except FileNotFoundError:
        pass

def add_task():
    task = input("Enter task: ")
    tasks.append({'task': task, 'completed': False})
    save_tasks()

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            save_tasks()
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def mark_completed():
    view_tasks()
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['completed'] = True
            save_tasks()
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    for idx, task in enumerate(tasks):
        status = "✔️" if task['completed'] else "❌"
        print(f"{idx + 1}. {task['task']} [{status}]")

load_tasks()

while True:
    print("\n1. Add Task\n2. Delete Task\n3. View Tasks\n4. Mark Completed\n5. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        delete_task()
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        mark_completed()
    elif choice == '5':
        break
    else:
        print("Invalid option.")
