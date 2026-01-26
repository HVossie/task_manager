# Task Manager (CLI)
Command-line task manager built with Python that supports full CRUD operations, filtering, and persistent storage using SQLite.

This project was built as a portfolio piece for me to practice clean Python design, data persistence, and user-safe input handling. It is intended to be my first portfolio project.

## Features

- Add, view, update, and delete tasks
- Mark tasks as completed
- Filter tasks by priority or completion status
- Persistent storage using SQLite
- Input validation to prevent crashes
- Simple, readable CLI interface

## Tech Stack

- Python 3
- SQLite
- Standard Library only (no external dependencies)

## How to Run

1. Clone the repository

```bash
git clone https://github.com/HVossie/task_manager.git
```

2. Navigate into the project:

```bash
cd task_manager
```

3. Run the application:

```bash
python main.py
```

## Project Structure

```bash
task_manager/
├── main.py       # CLI interface
├── task.py       # Task model
├── storage.py    # SQLite persistence layer
├── database.db   # Local database
└── README.md
```

## What I Learned

- Structuring a Python project with separation of concerns
- Using SQLite for lightweight persistence
- Writing defensive input validation
- Building a usable CLI application
- Version control with Git and GitHub

## Possible Improvements

- Add due date validation and sorting
- Export tasks to CSV
- Add unit tests
- Improve CLI UX

## Author

- Hanroux Vos