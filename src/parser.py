# src/parser.py

class ASTNode:
    """
    A simple class to represent a node in the Abstract Syntax Tree (AST).
    """
    def __init__(self, node_type, value=None, children=None):
        self.node_type = node_type
        self.value = value
        self.children = children or []

    def __repr__(self):
        return f"{self.node_type}: {self.value} -> {self.children}"

def parse(tokens):
    """
    Parse the list of tokens into an Abstract Syntax Tree (AST).
    """
    def expect(expected_type):
        """
        Ensure the current token is of the expected type.
        """
        if tokens and tokens[0][0] == expected_type:
            return tokens.pop(0)
        else:
            raise SyntaxError(f"Expected {expected_type} but found {tokens[0][0]}")

    # Start parsing
    ast = ASTNode("Program")
    while tokens:
        token_type, token_value = tokens[0]

        if token_type == 'ID' and token_value == 'print':
            tokens.pop(0)  # Remove 'print'
            expect('LPAREN')  # Expect '('
            
            # Accept either a STRING or an ID inside the print statement
            if tokens[0][0] == 'STRING':
                string_token = expect('STRING')  # Expect a string
                ast.children.append(ASTNode('Print', string_token[1]))
            elif tokens[0][0] == 'ID':
                id_token = expect('ID')  # Expect an identifier
                ast.children.append(ASTNode('PrintVar', id_token[1]))
            else:
                raise SyntaxError(f"Expected STRING or ID but found {tokens[0][0]}")
            
            expect('RPAREN')  # Expect ')'

        elif token_type == 'ID':  # Handle variable assignments
            id_token = tokens.pop(0)  # Remove the identifier
            expect('ASSIGN')  # Expect '=' for assignment
            value_token = expect('NUMBER')  # Expect a number for now (extend later)
            ast.children.append(ASTNode('Assign', id_token[1], [ASTNode('Number', value_token[1])]))

        elif token_type == 'NEWLINE':
            tokens.pop(0)  # Ignore newlines

        else:
            raise SyntaxError(f"Unexpected token: {token_type}")

    return ast
