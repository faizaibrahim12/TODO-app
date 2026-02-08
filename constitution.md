# Project Constitution

## Project Overview
This is a Phase I Todo In-Memory Python Console Application built using spec-driven development with Claude Code and Spec-Kit Plus.

## Development Principles

### 1. Spec-Driven Development
- All features must be specified before implementation
- Specifications are stored in `specs/` folder with version history
- Use Claude Code and Spec-Kit Plus for code generation

### 2. Clean Code Principles
- Follow PEP 8 Python style guidelines
- Write clear, self-documenting code
- Use type hints where appropriate
- Keep functions small and focused
- Single Responsibility Principle

### 3. Project Structure
```
/
├── constitution.md          # This file
├── specs/                   # Specification history
│   └── v1.0.0/
├── src/                     # Python source code
│   └── todo/
│       ├── __init__.py
│       ├── app.py          # Main application entry point
│       ├── models.py       # Task data models
│       └── commands.py     # Command handlers
├── README.md               # Setup and usage instructions
├── CLAUDE.md               # Claude Code instructions
└── pyproject.toml          # UV project configuration
```

### 4. Technology Stack
- **UV**: Fast Python package manager and project manager
- **Python 3.13+**: Latest Python version
- **Claude Code**: AI-powered code generation
- **Spec-Kit Plus**: Specification management

### 5. Feature Requirements
All Basic Level features must be implemented:
- ✅ Add tasks (with title and description)
- ✅ Delete tasks (by ID)
- ✅ Update tasks (modify title/description)
- ✅ View tasks (list all with status indicators)
- ✅ Mark tasks as complete/incomplete

### 6. Development Workflow
1. Write specification in `specs/` folder
2. Generate implementation plan
3. Break into tasks
4. Implement via Claude Code
5. Review and iterate

### 7. Code Quality Standards
- All code must be functional and tested manually
- No hardcoded values (use constants)
- Proper error handling
- User-friendly console interface

