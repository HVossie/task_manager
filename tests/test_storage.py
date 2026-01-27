import unittest
import os
from storage import Storage
from task import Task


class TestStorage(unittest.TestCase):
    TEST_DB = "test_database.db"

    def setUp(self):
        self.storage = Storage(self.TEST_DB)
        with self.storage._connect() as conn:
            conn.execute("DELETE FROM tasks")

    def test_add_and_get_task(self):
        task = Task("Test task")
        self.storage.add_task(task)

        tasks = self.storage.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Test task")

    def test_delete_task(self):
        task = Task("Delete me")
        task_id = self.storage.add_task(task)

        self.storage.delete_task(task_id)
        tasks = self.storage.get_all_tasks()
        self.assertEqual(len(tasks), 0)


if __name__ == "__main__":
    unittest.main()
