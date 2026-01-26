class Task:
    def __init__(self, title, description="", priority="medium", due_date=None, completed=False, task_id=None):
        self.id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title} (Priority: {self.priority}, Due: {self.due_date})"
