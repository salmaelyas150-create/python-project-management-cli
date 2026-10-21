# Python Project Management CLI

## Project Description

The Python Project Management CLI is a command-line application for managing users, projects, and tasks. It allows users to create and view users, create projects assigned to users, create and view project tasks, and mark tasks as completed.

The application uses Python, object-oriented programming (OOP), JSON file storage, `argparse` for command-line commands, and `Rich` for formatted terminal output.

## Features

- Create and list users.
- Create projects owned by existing users.
- View all projects or filter projects by user.
- Create tasks associated with existing projects.
- Assign tasks to registered users.
- View all tasks or filter tasks by project.
- Mark tasks as completed.
- Store users, projects, and tasks in local JSON files.
- Display formatted tables in the terminal.
- Validate user input and task statuses through the model classes.

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON for local data persistence
- `argparse` for command-line argument parsing
- `pytest` for automated testing

## Project Structure

```text
python-project-management-cli/
├── main.py
├── models/
│   ├── __init__.py
│   ├── person.py
│   ├── user.py
│   ├── project.py
│   └── task.py
├── utils/
│   ├── __init__.py
│   └── storage.py
├── data/
│   ├── users.json
│   ├── projects.json
│   └── tasks.json
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_storage.py
│   └── test_cli.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

- Python 3.10 or newer
- pip
- A terminal
- Git (optional, for cloning the repository)

## Installation and Setup

### 1. Clone the repository

Replace `YOUR-GITHUB-USERNAME` with your GitHub username.




### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

On Linux or WSL Ubuntu:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Prepare the data files

Create the data directory and initialize the JSON files if they do not already exist:

```bash
mkdir -p data
echo "[]" > data/users.json
echo "[]" > data/projects.json
echo "[]" > data/tasks.json
```


## Usage Instructions

Run commands from the project directory with the virtual environment activated.

### Display available commands

```bash
python main.py --help
```

### 1. Create a user

```bash
python main.py add-user --name "Alex" --email "alex@example.com"
```

### 2. List users

```bash
python main.py list-users
```

### 3. Create a project

The owner must already exist.

```bash
python main.py add-project --user "Alex" --title "CLI Tool" --description "Build a project tracker" --due-date "2026-12-01"
```

### 4. List projects

List all projects:

```bash
python main.py list-projects
```

Filter projects by user:

```bash
python main.py list-projects --user "Alex"
```

### 5. Create a task

The project must already exist. The assignee is optional but must be a registered user if provided.

```bash
python main.py add-task --project "CLI Tool" --title "Write the tests" --assigned-to "Alex"
```

### 6. List tasks

List all tasks:

```bash
python main.py list-tasks
```

Filter tasks by project:

```bash
python main.py list-tasks --project "CLI Tool"
```

### 7. Mark a task as completed

Use the task ID displayed when listing tasks.

```bash
python main.py complete-task --id task-1
```

### 8. Edit a task

If the edit command is implemented in `main.py`:

```bash
python main.py edit-task --id task-1 --title "Finish all project tests"
```

### 9. Delete a task

If the delete command is implemented in `main.py`:

```bash
python main.py delete-task --id task-1
```

## Data Persistence

Application data is stored locally in three JSON files:

- `data/users.json` stores registered users.
- `data/projects.json` stores project information.
- `data/tasks.json` stores task information.

The application loads records from these files and saves changes so that data can be used again when the application is restarted.

## Object-Oriented Programming

The application demonstrates OOP concepts through its model classes:

- **Inheritance:** `User` inherits from `Person`.
- **Encapsulation:** Properties protect access to values such as a person's email and a task's status.
- **Class attributes:** The model classes use class-level counters to track created objects.
- **Methods:** Users and projects can manage their associated projects and tasks.

## Running Tests

Run the automated tests with:

```bash
python -m pytest -q
```

To see which tests are collected:

```bash
python -m pytest --collect-only -q
```

## Limitations

This application stores data locally in JSON files. It is intended as a learning project and does not currently provide a database server or multi-user authentication system.

## Author

NAME:Salma Elyas.

**Project:** Python Project Management CLI Summative Lab
