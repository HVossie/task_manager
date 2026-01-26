from task import Task
from storage import Storage

storage = Storage()
VALID_PRIORITIES = {"low", "medium", "high"}


def print_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for t in tasks:
        status = "✔" if t.completed else "✘"
        print(f"[{status}] {t.id}: {t.title} (Priority: {t.priority})")


def add_task():
    title = get_non_empty_input("Title: ")
    priority = get_valid_priority()

    task = Task(title=title, priority=priority)
    task_id = storage.add_task(task)
    print(f"Task added with ID: {task_id}")


def view_tasks():
    tasks = storage.get_all_tasks()

    if not tasks:
        print("No tasks found.")
        return

    print("\nView options:")
    print("1. All tasks")
    print("2. Filter by priority")
    print("3. Filter by completed")
    print("4. Sort by due date")

    choice = input("Choose an option: ").strip()

    if choice == "2":
        priority = input("Enter priority (low/medium/high): ").strip().lower()
        tasks = [t for t in tasks if t.priority == priority]

    elif choice == "3":
        completed_choice = input("Show completed only? (yes/no): ").strip().lower()
        if completed_choice == "yes":
            tasks = [t for t in tasks if t.completed]
        else:
            tasks = [t for t in tasks if not t.completed]

    elif choice == "4":
        tasks = sorted(tasks, key=lambda x: x.due_date or "")

    print_tasks(tasks)


def mark_completed():
    task_id = get_valid_task_id()

    task = storage.get_task(task_id)
    if not task:
        print("Task not found.")
        return

    storage.complete_task(task_id)
    print("Task marked as completed.")


def delete_task():
    task_id = get_valid_task_id()

    task = storage.get_task(task_id)
    if not task:
        print("Task not found.")
        return

    storage.delete_task(task_id)
    print("Task deleted.")


def menu():
    while True:
        print("\n--- TASK MANAGER ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")

def get_valid_priority():
    while True:
        priority = input("Priority (low/medium/high): ").strip().lower()
        if priority in VALID_PRIORITIES:
            return priority
        print("Invalid priority. Choose low, medium, or high.")

def get_valid_task_id():
    while True:
        task_id = input("Enter task ID: ").strip()
        if task_id.isdigit():
            return int(task_id)
        print("Task ID must be a number.")

if __name__ == "__main__":
    menu()
