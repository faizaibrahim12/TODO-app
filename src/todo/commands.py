"""
Command parsing and execution for the todo application.
"""

import shlex
from typing import Optional

from .models import TodoStore, Task


class CommandHandler:
    """Handles command parsing and execution."""
    
    def __init__(self, store: TodoStore):
        """
        Initialize command handler with a task store.
        
        Args:
            store: TodoStore instance to operate on
        """
        self.store = store
    
    def parse_command(self, user_input: str) -> tuple[str, list[str]]:
        """
        Parse user input into command and arguments.
        
        Args:
            user_input: Raw user input string
            
        Returns:
            Tuple of (command, arguments)
        """
        if not user_input.strip():
            return "", []
        
        parts = shlex.split(user_input.strip())
        command = parts[0].lower() if parts else ""
        args = parts[1:] if len(parts) > 1 else []
        
        return command, args
    
    def execute(self, command: str, args: list[str]) -> str:
        """
        Execute a command with given arguments.
        
        Args:
            command: Command name
            args: Command arguments
            
        Returns:
            Result message string
        """
        if command in ("help", "?"):
            return self._help()
        elif command in ("exit", "quit", "q"):
            return "EXIT"
        elif command in ("add", "a"):
            return self._add_task(args)
        elif command in ("list", "view", "ls", "l"):
            return self._list_tasks()
        elif command in ("update", "edit", "u"):
            return self._update_task(args)
        elif command in ("delete", "remove", "del", "d"):
            return self._delete_task(args)
        elif command in ("complete", "done", "c"):
            return self._mark_complete(args)
        elif command in ("incomplete", "undone", "incomplete", "i"):
            return self._mark_incomplete(args)
        else:
            return f"Unknown command: {command}. Type 'help' for available commands."
    
    def _help(self) -> str:
        """Return help message."""
        return """
Available Commands:
  add <title> [description]     - Add a new task
  list, view                    - List all tasks
  update <id> [--title <title>] [--description <desc>] - Update a task
  delete <id>                   - Delete a task
  complete <id>                 - Mark task as complete
  incomplete <id>               - Mark task as incomplete
  help, ?                       - Show this help message
  exit, quit                    - Exit the application
"""
    
    def _add_task(self, args: list[str]) -> str:
        """Add a new task."""
        if not args:
            return "Error: Task title is required. Usage: add <title> [description]"
        
        title = args[0]
        description = " ".join(args[1:]) if len(args) > 1 else None
        
        task = self.store.add_task(title, description)
        return f"Task added successfully! ID: {task.id}"
    
    def _list_tasks(self) -> str:
        """List all tasks."""
        tasks = self.store.get_all_tasks()
        
        if not tasks:
            return "No tasks found. Add a task using 'add <title> [description]'"
        
        lines = ["\nAll Tasks:"]
        lines.append("-" * 60)
        
        for task in tasks:
            status = "[✓]" if task.completed else "[ ]"
            desc = f" - {task.description}" if task.description else ""
            lines.append(f"{status} ID: {task.id:3d} | {task.title}{desc}")
        
        lines.append("-" * 60)
        lines.append(f"Total: {len(tasks)} task(s)")
        
        return "\n".join(lines)
    
    def _update_task(self, args: list[str]) -> str:
        """Update a task."""
        if not args:
            return "Error: Task ID is required. Usage: update <id> [--title <title>] [--description <desc>]"
        
        try:
            task_id = int(args[0])
        except ValueError:
            return f"Error: Invalid task ID '{args[0]}'. ID must be a number."
        
        task = self.store.get_task(task_id)
        if not task:
            return f"Error: Task with ID {task_id} not found."
        
        # Parse optional arguments
        title = None
        description = None
        i = 1
        
        while i < len(args):
            if args[i] == "--title" and i + 1 < len(args):
                title = args[i + 1]
                i += 2
            elif args[i] == "--description" and i + 1 < len(args):
                description = args[i + 1]
                i += 2
            elif args[i].startswith("--"):
                return f"Error: Unknown option '{args[i]}'. Use --title or --description."
            else:
                # If no flag, treat remaining as description
                description = " ".join(args[i:])
                break
        
        task.update(title, description)
        return f"Task {task_id} updated successfully!"
    
    def _delete_task(self, args: list[str]) -> str:
        """Delete a task."""
        if not args:
            return "Error: Task ID is required. Usage: delete <id>"
        
        try:
            task_id = int(args[0])
        except ValueError:
            return f"Error: Invalid task ID '{args[0]}'. ID must be a number."
        
        if self.store.delete_task(task_id):
            return f"Task {task_id} deleted successfully!"
        else:
            return f"Error: Task with ID {task_id} not found."
    
    def _mark_complete(self, args: list[str]) -> str:
        """Mark a task as complete."""
        if not args:
            return "Error: Task ID is required. Usage: complete <id>"
        
        try:
            task_id = int(args[0])
        except ValueError:
            return f"Error: Invalid task ID '{args[0]}'. ID must be a number."
        
        task = self.store.get_task(task_id)
        if not task:
            return f"Error: Task with ID {task_id} not found."
        
        task.mark_complete()
        return f"Task {task_id} marked as complete!"
    
    def _mark_incomplete(self, args: list[str]) -> str:
        """Mark a task as incomplete."""
        if not args:
            return "Error: Task ID is required. Usage: incomplete <id>"
        
        try:
            task_id = int(args[0])
        except ValueError:
            return f"Error: Invalid task ID '{args[0]}'. ID must be a number."
        
        task = self.store.get_task(task_id)
        if not task:
            return f"Error: Task with ID {task_id} not found."
        
        task.mark_incomplete()
        return f"Task {task_id} marked as incomplete!"

