#type: ignore
import unittest
from task import Task
import sqlite3

# -----------------------------
# In-memory Storage for testing
# -----------------------------
class InMemoryStorage:
    def __init__(self):
        self.conn = sqlite3.connect(":memory:", check_same_thread=False)
        self._create_table()

    def _create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                priority TEXT,
                due_date TEXT,
                completed INTEGER
            )
        """)

    def _execute(self, query, params=()):
        cur = self.conn.execute(query, params)
        self.conn.commit()
        return cur

    def add_task(self, task):
        cur = self._execute(
            "INSERT INTO tasks (title, description, priority, due_date, completed) VALUES (?, ?, ?, ?, ?)",
            (task.title, task.description, task.priority, task.due_date, int(task.completed))
        )
        return cur.lastrowid

    def get_task(self, task_id):
        row = self._execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
        if row:
            return Task(row[1], row[2], row[3], row[4], bool(row[5]), task_id=row[0])
        return None

    def get_all_tasks(self):
        rows = self._execute("SELECT * FROM tasks").fetchall()
        return [Task(row[1], row[2], row[3], row[4], bool(row[5]), task_id=row[0]) for row in rows]

    def delete_task(self, task_id):
        self._execute("DELETE FROM tasks WHERE id = ?", (task_id,))

    def complete_task(self, task_id):
        self._execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))

    def update_task(self, task_id, **kwargs):
        fields = ', '.join(f"{k} = ?" for k in kwargs)
        values = list(kwargs.values()) + [task_id]
        self._execute(f"UPDATE tasks SET {fields} WHERE id = ?", values)

    def clear_tasks(self):
        self._execute("DELETE FROM tasks")

# -----------------------------
# Unit tests using InMemoryStorage
# -----------------------------
class TestStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.storage = InMemoryStorage()

    def setUp(self):
        self.storage.clear_tasks()

    def test_add_and_get_task(self):
        task = Task("Test task", priority="medium", completed=False)
        task_id = self.storage.add_task(task)
        fetched_task = self.storage.get_task(task_id)
        self.assertIsNotNone(fetched_task)
        self.assertEqual(fetched_task.title, "Test task")

    def test_delete_task(self):
        task = Task("Delete me")
        task_id = self.storage.add_task(task)
        self.storage.delete_task(task_id)
        self.assertIsNone(self.storage.get_task(task_id))

    def test_complete_task(self):
        task = Task("Complete me", completed=False)
        task_id = self.storage.add_task(task)
        self.storage.complete_task(task_id)
        self.assertTrue(self.storage.get_task(task_id).completed)

    def test_update_task_priority(self):
        task = Task("Update me", priority="low")
        task_id = self.storage.add_task(task)
        self.storage.update_task(task_id, priority="high")
        self.assertEqual(self.storage.get_task(task_id).priority, "high")

    def test_get_all_tasks(self):
        t1 = Task("Task1", priority="low")
        t2 = Task("Task2", priority="medium")
        self.storage.add_task(t1)
        self.storage.add_task(t2)

        all_tasks = self.storage.get_all_tasks()
        self.assertEqual(len(all_tasks), 2)
        self.assertTrue(any(t.title == "Task1" for t in all_tasks))
        self.assertTrue(any(t.title == "Task2" for t in all_tasks))


if __name__ == "__main__":
    unittest.main()