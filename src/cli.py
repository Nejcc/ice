import sys
import os

# Absolute imports for compiler and interpreter modules
from src.compiler import compile_ice
from src.interpreter import run_ice

def build(file):
    """
    Function to build (compile) an ICE source file.
    """
    print(f"Building {file}...")
    compile_ice(file)

def run(file):
    """
    Function to run (interpret) an ICE source file.
    """
    print(f"Running {file}...")
    run_ice(file)

def main():
    """
    Main function to handle CLI commands for the ICE language.
    """
    # Ensure the correct number of arguments are provided
    if len(sys.argv) < 3:
        print("Usage: ice [command] [file.ice]")
        return

    # Parse the command and file from arguments
    command = sys.argv[1]
    file = sys.argv[2]

    # Check if the file has the correct extension
    if not file.endswith('.ice'):
        print("Error: The file must have a .ice extension")
        return

    # Check if the file exists
    if not os.path.exists(file):
        print("Error: File not found")
        return

    # Determine which command to execute
    if command == 'build':
        build(file)
    elif command == 'run':
        run(file)
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
