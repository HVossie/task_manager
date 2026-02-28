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
- Windows-safe unit tests using  in-memory SQLite database
- Modular design with clear separation of concerns

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

4. Run the unit tests

```bash
python -m unittest discover -s tests -p "test_*.py"
```
All tests are Windows-safe and use an in-memory database.

## Project Structure

```bash
task_manager/
├── main.py       # CLI interface
├── task.py       # Task model
├── storage.py    # SQLite persistence layer
├── database.db   # Local database
├── tests/        # Unit tests
│   ├── test_task.py
│   └── test_storage.py
└── README.md
```

## What I Learned

- Structuring a Python project with separation of concerns
- Writing unit tests for data models and database interactions
- Using SQLite for lightweight persistence
- Implementing defensive input validation
- Building a usable CLI application
- Version control with Git and GitHub

## Possible Improvements

- Add due date validation and sorting
- Export tasks to CSV or JSON
- Add more automated tests for edge cases
- Improve CLI UX (colors, menus)

## Author

- Hanroux Vos