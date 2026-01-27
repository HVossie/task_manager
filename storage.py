import sqlite3
from task import Task


class Storage:
    def __init__(self, db_path="database.db"):
        self.db_path = db_path
        self._create_table()

    def _connect(self):
        return sqlite3.connect(self.db_path, check_same_thread=False)

    def _create_table(self):
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
        with self._connect() as conn:
            cursor = conn.execute("""
                INSERT INTO tasks (title, description, priority, due_date, completed)
                VALUES (?, ?, ?, ?, ?)
            """, (task.title, task.description, task.priority, task.due_date, int(task.completed)))
            return cursor.lastrowid

    def get_all_tasks(self):
        with self._connect() as conn:
            rows = conn.execute("SELECT * FROM tasks").fetchall()
            return [
                Task(row[1], row[2], row[3], row[4], bool(row[5]), task_id=row[0])
                for row in rows
            ]

    def get_task(self, task_id):
        with self._connect() as conn:
            row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
            if row:
                return Task(row[1], row[2], row[3], row[4], bool(row[5]), task_id=row[0])
            return None

    def update_task(self, task_id, **kwargs):
        fields = []
        values = []
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
        self.update_task(task_id, completed=1)

    def delete_task(self, task_id):
        with self._connect() as conn:
            conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
