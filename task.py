"""
Task model for the Task Manager application.

Represents a single task and its associated data.
This class acts as a data container between the CLI and the database stroage layer.
"""
class Task:
    """
    Represents an individual task.

    Attributes:
        id (int | None): Database ID assigned by SQLite.
        title (str): Short name of the task.
        description (str): Optional detailed description.
        priority (str): Task priority (low, medium, high).
        due_date (str | None): Optional due date.
        completed (bool): Completion status. 
    """
    def __init__(self, title, description="", priority="medium", due_date=None, completed=False, task_id=None):
        """
        Initialize a new Task instance.

        task_id is optional because it is assigned automatically 
        when stored in the database
        """
        #Database identifier
        self.id = task_id

        #Core task information
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date

        #Task state
        self.completed = completed

    def mark_completed(self):
        """
        Mark this task as completed locally.

        Note:
        This updates only the object in memory.
        The Storage class must be used to persist the change to the database.
        """
        self.completed = True

    def __str__(self):
        """
        Returns a readable string representation used when displaying tasks in the CLI
        """
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title} (Priority: {self.priority}, Due: {self.due_date})"
    