# Todo Application - Phase I

A command-line todo application that stores tasks in memory, built using spec-driven development with Claude Code and Spec-Kit Plus.

## Features

- ✅ **Add Tasks**: Create new tasks with title and optional description
- ✅ **View Tasks**: List all tasks with status indicators
- ✅ **Update Tasks**: Modify task title and/or description
- ✅ **Delete Tasks**: Remove tasks by ID
- ✅ **Mark Complete/Incomplete**: Toggle task completion status

## Prerequisites

### Windows Users: WSL 2 Setup

Windows users must use WSL 2 (Windows Subsystem for Linux) for development:

```bash
# Install WSL 2
wsl --install

# Set WSL 2 as default
wsl --set-default-version 2

# Install Ubuntu
wsl --install -d Ubuntu-22.04
```

### Required Software

- **UV**: Fast Python package manager
- **Python 3.13+**: Latest Python version

## Installation

### 1. Install UV

On Linux/macOS:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows (WSL 2):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Clone and Setup Project

```bash
# Navigate to project directory
cd todo

# Install project dependencies (if any)
uv sync

# Or create virtual environment
uv venv
source .venv/bin/activate  # On Windows WSL: source .venv/bin/activate
```

## Usage

### Running the Application

```bash
# Using UV
uv run python -m todo.app

# Or if installed as package
uv run todo

# Or directly with Python
python -m todo.app
```

### Available Commands

Once the application is running, you can use the following commands:

- `add <title> [description]` - Add a new task
- `list` or `view` - List all tasks
- `update <id> [--title <title>] [--description <desc>]` - Update a task
- `delete <id>` - Delete a task
- `complete <id>` - Mark task as complete
- `incomplete <id>` - Mark task as incomplete
- `help` or `?` - Show help message
- `exit` or `quit` - Exit the application

### Example Session

```
todo> add "Buy groceries" "Milk, eggs, bread"
Task added successfully! ID: 1

todo> add "Finish project report"
Task added successfully! ID: 2

todo> list

All Tasks:
------------------------------------------------------------
[ ] ID:   1 | Buy groceries - Milk, eggs, bread
[ ] ID:   2 | Finish project report
------------------------------------------------------------
Total: 2 task(s)

todo> complete 1
Task 1 marked as complete!

todo> update 2 --description "Due by Friday"
Task 2 updated successfully!

todo> list

All Tasks:
------------------------------------------------------------
[✓] ID:   1 | Buy groceries - Milk, eggs, bread
[ ] ID:   2 | Finish project report - Due by Friday
------------------------------------------------------------
Total: 2 task(s)

todo> delete 1
Task 1 deleted successfully!

todo> exit
Goodbye!
```

## Project Structure

```
/
├── constitution.md          # Project constitution and principles
├── specs/                   # Specification history
│   └── v1.0.0/
│       └── todo-app-spec.md
├── src/                     # Python source code
│   └── todo/
│       ├── __init__.py
│       ├── app.py          # Main application entry point
│       ├── models.py       # Task data models
│       └── commands.py     # Command handlers
├── README.md               # This file
├── CLAUDE.md               # Claude Code instructions
└── pyproject.toml          # UV project configuration
```

## Development

This project follows spec-driven development:

1. Specifications are stored in `specs/` folder
2. Code is generated using Claude Code and Spec-Kit Plus
3. All features are implemented according to specifications

## Technology Stack

- **UV**: Fast Python package manager and project manager
- **Python 3.13+**: Latest Python version
- **Claude Code**: AI-powered code generation
- **Spec-Kit Plus**: Specification management

## License

This project is part of a development exercise.

"# TODO-app" 
