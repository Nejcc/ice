# src/interpreter.py

from src.lexer import tokenize
from src.parser import parse

def run_ice(file_path):
    """
    Function to interpret and run an ICE source file.
    """
    print(f"Running {file_path}...")

    try:
        with open(file_path, 'r') as file:
            source_code = file.read()
            # Tokenize and parse
            tokens = tokenize(source_code)
            ast = parse(tokens)
            
            # Interpret the AST
            interpret(ast)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except SyntaxError as e:
        print(f"Syntax error: {e}")

def interpret(ast):
    """
    Interpret the AST and execute the code.
    """
    for node in ast.children:
        if node.node_type == 'Print':
            print(node.value)  # Execute print statement
