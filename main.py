from storage import Storage
from task import Task

storage = Storage()

task = Task("Finish portfolio project", "Build SQLite", "high", "2026-02-01")
task_id = storage.add_task(task)
print("Saved task with ID:", task_id)

tasks = storage.get_all_tasks()
for t in tasks:
    print(t)
