import unittest
from task import Task


class TestTask(unittest.TestCase):

    def test_task_creation(self):
        task = Task(
            title="Write unit tests",
            description="Practice unittest",
            priority="high",
            due_date="2026-02-01"
        )

        self.assertEqual(task.title, "Write unit tests")
        self.assertEqual(task.priority, "high")
        self.assertFalse(task.completed)

    def test_mark_completed(self):
        task = Task("Finish project")
        task.mark_completed()

        self.assertTrue(task.completed)


if __name__ == "__main__":
    unittest.main()
