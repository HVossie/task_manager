"""
Command Line Interface (CLI) for the Task Manager

This module handles:
- User interaction
- Input validation
- Menu navigation
- Displaying tasks

All database operations are handled by the Storage class.
"""

from task import Task
from storage import Storage

# Single storage instance used throughout the application
storage = Storage()

# Allowed priority values for validation
VALID_PRIORITIES = {"low", "medium", "high"}

# --- Menu constants for readability ---
ADD_TASK = 1
VIEW_TASKS = 2
MARK_COMPLETED = 3
DELETE_TASK = 4
EXIT = 5

# View task options
VIEW_ALL = 1
VIEW_BY_PRIORITY = 2
VIEW_BY_COMPLETED = 3
SORT_BY_DUE_DATE = 4

# ---------------------- Helper Functions ----------------------

def get_int_input(prompt, min_value=None, max_value=None):
    """
    Request an integer from the user.
    Continue prompting until:
    - a valid integer is entered
    - optional min/max constraints are satisfied
    """
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Please enter a number >= {min_value}")
                continue
            if max_value is not None and value > max_value:
                print(f"Please enter a number <= {max_value}")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number")

def get_non_empty_input(prompt):
    """
    Ensure user input is not empty
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")

def get_valid_priority():
    """
    Validate priority input against allowed values.
    """
    while True:
        priority = input("Priority (low/medium/high): ").strip().lower()
        if priority in VALID_PRIORITIES:
            return priority
        print("Invalid priority. Choose low, medium, or high.")

def get_valid_task_id():
    """
    Request a valid task ID from the user.
    Ensures:
    - task exists
    - input is numeric
    """
    tasks = storage.get_all_tasks()
    if not tasks:
        print("No tasks available.")
        return None

    valid_ids = {task.id for task in tasks}
    while True:
        task_id = input("Enter task ID: ").strip()
        if task_id.isdigit() and int(task_id) in valid_ids:
            return int(task_id)
        print("Invalid task ID")

def print_tasks(tasks):
    """
    Display tasks in a readable CLI format.
    """
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
        status = "✔" if t.completed else "✘"
        print(f"[{status}] {t.id}: {t.title} (Priority: {t.priority})")

# ---------------------- Core Functionality ----------------------

def add_task():
    """
    Create a new task based on user input.
    """
    title = get_non_empty_input("Title: ")
    priority = get_valid_priority()

    task = Task(title=title, priority=priority)
    task_id = storage.add_task(task)
    print(f"Task added with ID: {task_id}")

def view_tasks():
    """
    Display tasks with optional filtering and sorting options.
    """
    tasks = storage.get_all_tasks()
    if not tasks:
        print("No tasks found.")
        return

    print("\nView options:")
    print(f"{VIEW_ALL}. All tasks")
    print(f"{VIEW_BY_PRIORITY}. Filter by priority")
    print(f"{VIEW_BY_COMPLETED}. Filter by completed")
    print(f"{SORT_BY_DUE_DATE}. Sort by due date")

    choice = get_int_input("Choose an option: ", VIEW_ALL, SORT_BY_DUE_DATE)

    if choice == VIEW_BY_PRIORITY:
        priority = input("Enter priority (low/medium/high): ").strip().lower()
        tasks = [t for t in tasks if t.priority == priority]
    elif choice == VIEW_BY_COMPLETED:
        completed_choice = input("Show completed only? (yes/no): ").strip().lower()
        if completed_choice == "yes":
            tasks = [t for t in tasks if t.completed]
        else:
            tasks = [t for t in tasks if not t.completed]
    elif choice == SORT_BY_DUE_DATE:
        tasks = sorted(tasks, key=lambda x: x.due_date or "")

    # VIEW_ALL leaves tasks unchanged
    print_tasks(tasks)

def mark_completed():
    """
    Mark an existing task as completed.
    """
    task_id = get_valid_task_id()
    if task_id is None:
        return
    storage.complete_task(task_id)
    print("Task marked as completed.")

def delete_task():
    """
    Delete a task selected by user.
    """
    task_id = get_valid_task_id()
    if task_id is None:
        return
    storage.delete_task(task_id)
    print("Task deleted.")

# ---------------------- Main Menu ----------------------

def menu():
    """
    Main application loop.
    Displays menu options and routes user choices to the appropriate functionality.
    """
    while True:
        print("\n--- TASK MANAGER ---")
        print(f"{ADD_TASK}. Add task")
        print(f"{VIEW_TASKS}. View tasks")
        print(f"{MARK_COMPLETED}. Mark task as completed")
        print(f"{DELETE_TASK}. Delete task")
        print(f"{EXIT}. Exit")

        choice = get_int_input("Choose an option: ", ADD_TASK, EXIT)

        if choice == ADD_TASK:
            add_task()
        elif choice == VIEW_TASKS:
            view_tasks()
        elif choice == MARK_COMPLETED:
            mark_completed()
        elif choice == DELETE_TASK:
            delete_task()
        elif choice == EXIT:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# ---------------------- Entry Point ----------------------

if __name__ == "__main__":
    menu()