"""
SQLite persistence layer for the Task Manager application

This module is responsible for all database operations:
- Creating the database table
- Adding tasks
- Retrieving tasks
- Updating tasks
- Deleting tasks

The CLI never interacts directly with SQLite - it communicates through
this Storage class instead. This keeps database logic separate from 
user interface logic.
"""

import sqlite3
from task import Task


class Storage:
    """
    Handles all interactions with the SQLite database.
    """
    def __init__(self, db_path="database.db"):
        """
        Initialize storage with a database path.

        Automatically creates the tasks table if it does not exist
        """
        self.db_path = db_path
        self._create_table()

    def _connect(self):
        """
        Create and return a new database connection

        check_same_thread=False allows connections to be used safely
        across different parts of the application.
        """
        return sqlite3.connect(self.db_path, check_same_thread=False)

    def _create_table(self):
        """
        Create the task table if it does not already exist
        """
        with self._connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    priority TEXT,
                    due_date TEXT,
                    completed INTEGER
                )
            """)

    def add_task(self, task: Task):
        """
        Insert a new task into the database

        Returns:
            int: ID of the newly created task.
        """
        with self._connect() as conn:
            cursor = conn.execute("""
                INSERT INTO tasks (title, description, priority, due_date, completed)
                VALUES (?, ?, ?, ?, ?)
            """, (task.title, task.description, task.priority, task.due_date, int(task.completed)))
            return cursor.lastrowid

    def get_all_tasks(self):
        """
        Retrieve all tasks from the database

        Returns:
            list[Task]: list of task objects.
        """
        with self._connect() as conn:
            rows = conn.execute("SELECT * FROM tasks").fetchall()
            return [
                Task(row[1], row[2], row[3], row[4], bool(row[5]), task_id=row[0])
                for row in rows
            ]

    def get_task(self, task_id):
        """
        Retrieve a single task by its ID

        Returns:
            Task | None
        """
        with self._connect() as conn:
            row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
            if row:
                return Task(row[1], row[2], row[3], row[4], bool(row[5]), task_id=row[0])
            return None

    def update_task(self, task_id, **kwargs):
        """
        Update one or more fields of a task dynamically

        Example:
            update_task(1, completed=1, priority="high")

        kwargs allows flexible updates without writing
        separate update functions for each field.
        """
        fields = []
        values = []

        #Build SQL dynamically from provided fields
        for key, value in kwargs.items():
            fields.append(f"{key} = ?")
            values.append(value)
        values.append(task_id)

        with self._connect() as conn:
            conn.execute(f"""
                UPDATE tasks
                SET {', '.join(fields)}
                WHERE id = ?
            """, values)

    def complete_task(self, task_id):
        """
        Mark a task as completed
        """
        self.update_task(task_id, completed=1)

    def delete_task(self, task_id):
        """
        Permanently remove a task from the database.
        """
        with self._connect() as conn:
            conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
