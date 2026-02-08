# Claude Code Instructions

This document provides instructions for using Claude Code to work with this Todo Application project.

## Project Overview

This is a Phase I Todo In-Memory Python Console Application built using spec-driven development. The project follows the Agentic Dev Stack workflow: Write spec → Generate plan → Break into tasks → Implement via Claude Code.

## Project Structure

```
/
├── constitution.md          # Project constitution and development principles
├── specs/                   # Specification history
│   └── v1.0.0/
│       └── todo-app-spec.md # Current specification version
├── src/                     # Python source code
│   └── todo/
│       ├── __init__.py
│       ├── app.py          # Main CLI loop and entry point
│       ├── models.py       # Task class and TodoStore
│       └── commands.py     # Command parsing and execution
├── README.md               # Setup and usage instructions
├── CLAUDE.md               # This file
└── pyproject.toml          # UV project configuration
```

## Development Workflow

### 1. Specification-Driven Development

All features must be specified before implementation:

- Specifications are stored in `specs/v1.0.0/todo-app-spec.md`
- Review the specification before making changes
- Update specifications when requirements change
- Create new version folders for major specification changes

### 2. Code Generation with Claude Code

When implementing features:

1. **Read the specification** in `specs/v1.0.0/todo-app-spec.md`
2. **Review existing code** in `src/todo/` to understand the structure
3. **Generate code** following the patterns established in the codebase
4. **Follow clean code principles** as outlined in `constitution.md`

### 3. Code Organization

The codebase is organized into modules:

- **`models.py`**: Contains `Task` class and `TodoStore` class
  - `Task`: Represents a single todo task with id, title, description, status
  - `TodoStore`: In-memory storage for tasks with CRUD operations

- **`commands.py`**: Contains `CommandHandler` class
  - Parses user input into commands and arguments
  - Executes commands and returns result messages
  - Handles all user interactions

- **`app.py`**: Main application entry point
  - Initializes the todo store and command handler
  - Runs the interactive CLI loop
  - Handles user input/output

### 4. Adding New Features

When adding new features:

1. **Update specification** in `specs/v1.0.0/todo-app-spec.md` (or create new version)
2. **Update `CommandHandler`** in `commands.py` to handle new commands
3. **Update `TodoStore`** in `models.py` if new data operations are needed
4. **Update help text** in `CommandHandler._help()` method
5. **Test manually** to ensure feature works correctly

### 5. Code Style Guidelines

Follow these guidelines when generating code:

- **PEP 8**: Follow Python style guidelines
- **Type Hints**: Use type hints for function parameters and return values
- **Docstrings**: Include docstrings for all classes and public methods
- **Error Handling**: Provide clear, user-friendly error messages
- **Constants**: Use constants for magic strings/numbers
- **Single Responsibility**: Each function/class should have one clear purpose

### 6. Example: Adding a New Command

To add a new command (e.g., "search"):

1. Add command specification to `specs/v1.0.0/todo-app-spec.md`
2. Add command parsing in `CommandHandler.parse_command()` (if needed)
3. Add command execution in `CommandHandler.execute()`:
   ```python
   elif command in ("search", "find", "s"):
       return self._search_tasks(args)
   ```
4. Implement `_search_tasks()` method in `CommandHandler`
5. Update help text in `_help()` method

### 7. Testing the Application

Run the application:
```bash
uv run python -m todo.app
```

Test all commands:
- Add tasks with and without descriptions
- List tasks
- Update tasks
- Delete tasks
- Mark tasks complete/incomplete
- Test error cases (invalid IDs, missing arguments)

### 8. Common Patterns

**Command Parsing:**
```python
command, args = handler.parse_command(user_input)
result = handler.execute(command, args)
```

**Task Operations:**
```python
# Get task
task = store.get_task(task_id)
if not task:
    return f"Error: Task {task_id} not found."

# Update task
task.update(title="New Title", description="New Description")

# Mark complete
task.mark_complete()
```

**Error Handling:**
```python
try:
    task_id = int(args[0])
except ValueError:
    return f"Error: Invalid task ID '{args[0]}'. ID must be a number."
```

## Key Principles

1. **No Manual Coding**: All code should be generated via Claude Code
2. **Spec-First**: Always refer to specifications before coding
3. **Clean Code**: Follow principles in `constitution.md`
4. **User-Friendly**: Provide clear error messages and help text
5. **In-Memory Only**: No file I/O or database (Phase I requirement)

## Questions for Claude Code

When working on this project, you can ask Claude Code:

- "Add a search feature to find tasks by keyword"
- "Improve the list command to show tasks sorted by creation date"
- "Add validation to prevent empty task titles"
- "Refactor the command handler to use a command pattern"

Always ensure Claude Code:
1. Reads the relevant specification
2. Understands the existing code structure
3. Follows the established patterns
4. Updates help text and documentation as needed

