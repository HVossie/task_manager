# Task Manager (CLI)

A command-line task manager built with Python that supports creating, viewing, completing, and deleting tasks with persistent SQLite storage.

This project was built to practice clean Python structure, data persistence, input validation, and modular design in a small but complete application.

## Features

- Add new tasks
- View all tasks
- Filter tasks by priority
- Filter tasks by completion status
- Sort tasks by due date
- Mark tasks as completed
- Delete tasks
- Persistent storage using SQLite
- Input validation to prevent crashes from invalid user input
- Modular design with clear separation between the CLI, task model, and storage layer
- Unit tests using an isolated test database

## Tech Stack

- Python 3
- SQLite
- Python Standard Library only

## How to Run

1. Clone the repository

```bash
git clone https://github.com/HVossie/task_manager.git
```

2. Navigate into the project

```bash
cd task_manager
```

3. Run the application

```bash
python main.py
```

4. Run the tests

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Project Structure

```text
task_manager/
|-- main.py       # CLI interface and menu flow
|-- task.py       # Task data model
|-- storage.py    # SQLite persistence layer
|-- database.db   # Local application database
|-- tests/
|   |-- test_task.py
|   `-- test_storage.py
`-- README.md
```

## What I Learned

- Structuring a Python project with separation of concerns
- Writing unit tests for models and database operations
- Using SQLite for lightweight persistent storage
- Validating user input in a CLI application
- Building a small application with readable, maintainable code
- Using Git and GitHub to track and publish project work

## Possible Improvements

- Add due date input and validation to task creation
- Add task editing from the CLI
- Export tasks to CSV or JSON
- Expand test coverage for more edge cases
- Improve CLI presentation and formatting

## Author

- Hanroux Vos
