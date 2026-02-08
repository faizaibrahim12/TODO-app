"""
Task data models for the todo application.
"""

from datetime import datetime
from typing import Optional


class Task:
    """Represents a single todo task."""
    
    def __init__(self, task_id: int, title: str, description: Optional[str] = None):
        """
        Initialize a new task.
        
        Args:
            task_id: Unique identifier for the task
            title: Task title (required)
            description: Task description (optional)
        """
        self.id = task_id
        self.title = title
        self.description = description or ""
        self.completed = False
        self.created_at = datetime.now()
    
    def mark_complete(self) -> None:
        """Mark the task as complete."""
        self.completed = True
    
    def mark_incomplete(self) -> None:
        """Mark the task as incomplete."""
        self.completed = False
    
    def update(self, title: Optional[str] = None, description: Optional[str] = None) -> None:
        """
        Update task details.
        
        Args:
            title: New title (if provided)
            description: New description (if provided)
        """
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
    
    def __str__(self) -> str:
        """String representation of the task."""
        status = "[✓]" if self.completed else "[ ]"
        desc = f" - {self.description}" if self.description else ""
        return f"{status} {self.id}: {self.title}{desc}"
    
    def __repr__(self) -> str:
        """Developer representation of the task."""
        return f"Task(id={self.id}, title='{self.title}', completed={self.completed})"


class TodoStore:
    """In-memory storage for todo tasks."""
    
    def __init__(self):
        """Initialize an empty task store."""
        self.tasks: dict[int, Task] = {}
        self.next_id = 1
    
    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Add a new task to the store.
        
        Args:
            title: Task title
            description: Task description (optional)
            
        Returns:
            The newly created Task
        """
        task = Task(self.next_id, title, description)
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Get a task by ID.
        
        Args:
            task_id: Task identifier
            
        Returns:
            Task if found, None otherwise
        """
        return self.tasks.get(task_id)
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by ID.
        
        Args:
            task_id: Task identifier
            
        Returns:
            True if task was deleted, False if not found
        """
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False
    
    def get_all_tasks(self) -> list[Task]:
        """
        Get all tasks.
        
        Returns:
            List of all tasks
        """
        return list(self.tasks.values())
    
    def task_count(self) -> int:
        """
        Get the total number of tasks.
        
        Returns:
            Number of tasks in the store
        """
        return len(self.tasks)

