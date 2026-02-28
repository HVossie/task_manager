import unittest
from task import Task


class TestTask(unittest.TestCase):

    def test_task_creation(self):
        """
        Task attributes are correctly initialized.
        """
        task = Task(
            title="Write unit tests",
            description="Practice unittest",
            priority="high",
            due_date="2026-02-01"
        )

        self.assertEqual(task.title, "Write unit tests")
        self.assertEqual(task.description, "Practice unittest")
        self.assertEqual(task.priority, "high")
        self.assertEqual(task.due_date, "2026-02-01")
        self.assertFalse(task.completed)

    def test_mark_completed(self):
        """
        mark_completed() correctly updates the completed flag.
        """
        task = Task("Finish project")
        task.mark_completed()
        self.assertTrue(task.completed)

    def test_str_representation(self):
        """
        __str__ returns a readable format for the CLI.
        """
        task = Task("Test Task", completed=True, priority="medium", due_date="2026-02-28")
        output = str(task)
        self.assertIn("✓", output)
        self.assertIn("Test Task", output)
        self.assertIn("medium", output)
        self.assertIn("2026-02-28", output)


if __name__ == "__main__":
    unittest.main()