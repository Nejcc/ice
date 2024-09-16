from src.lexer import tokenize
from src.parser import parse, ASTNode  # Import ASTNode class

variables = {}

def run_ice(file_path):
    print(f"Running {file_path}...")

    try:
        with open(file_path, 'r') as file:
            source_code = file.read()
            tokens = tokenize(source_code)
            ast = parse(tokens)
            interpret(ast)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except SyntaxError as e:
        print(f"Syntax error: {e}")

def interpret(ast):
    for node in ast.children:
        if node.node_type == 'Print':
            print(node.value)
        elif node.node_type == 'PrintVar':
            if node.value in variables:
                print(variables[node.value])
            else:
                print(f"Error: Variable '{node.value}' not defined.")
        elif node.node_type == 'Assign':
            result = evaluate(node.children[0])
            variables[node.value] = result
            print(f"{node.value} = {result}")
        elif node.node_type == 'If':
            condition = evaluate_condition(node.children[0])
            if condition:
                for statement in node.children[1:]:
                    interpret(ASTNode("Program", None, [statement]))

def evaluate(node):
    if node.node_type == 'Number':
        return node.value
    elif node.node_type == 'Variable':
        if node.value in variables:
            return variables[node.value]
        else:
            raise RuntimeError(f"Variable '{node.value}' not defined.")
    elif node.node_type == 'Operation':
        left = evaluate(node.children[0])
        right = evaluate(node.children[1])
        if node.value == '+':
            return left + right
        elif node.value == '-':
            return left - right
        elif node.value == '*':
            return left * right
        elif node.value == '/':
            return left / right
        else:
            raise RuntimeError(f"Unknown operator: {node.value}")

def evaluate_condition(node):
    left = evaluate(node.children[0])
    right = evaluate(node.children[1])
    if node.value == '==':
        return left == right
    elif node.value == '!=':
        return left != right
    elif node.value == '<':
        return left < right
    elif node.value == '>':
        return left > right
    elif node.value == '<=':
        return left <= right
    elif node.value == '>=':
        return left >= right
    else:
        raise RuntimeError(f"Unknown comparison operator: {node.value}")
