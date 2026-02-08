"""
Main application entry point for the todo console application.
"""

from .models import TodoStore
from .commands import CommandHandler


def main():
    """Main application loop."""
    print("=" * 60)
    print("Welcome to Todo Application v1.0.0")
    print("Type 'help' for available commands or 'exit' to quit")
    print("=" * 60)
    print()
    
    store = TodoStore()
    handler = CommandHandler(store)
    
    while True:
        try:
            user_input = input("todo> ").strip()
            
            if not user_input:
                continue
            
            command, args = handler.parse_command(user_input)
            result = handler.execute(command, args)
            
            if result == "EXIT":
                print("Goodbye!")
                break
            
            print(result)
            print()
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except EOFError:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            print()


if __name__ == "__main__":
    main()

