# todo_app.py
tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for i, t in enumerate(tasks, 1):
        status = "✓" if t["done"] else "✗"
        print(f"{i}. {t['task']} [{status}]")

def delete_task():
    view_tasks()
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(idx)
        print(f"Task '{removed['task']}' deleted.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def mark_done():
    view_tasks()
    try:
        idx = int(input("Enter task number to mark as done: ")) - 1
        tasks[idx]["done"] = True
        print(f"Task '{tasks[idx]['task']}' marked as done.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def main():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
