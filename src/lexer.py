# src/lexer.py

import re

def tokenize(source_code):
    """
    Tokenize the input source code into a list of tokens.
    """
    tokens = []
    
    # Define a basic set of token rules
    token_specification = [
        ('NUMBER',   r'\d+(\.\d*)?'),   # Integer or decimal number
        ('STRING',   r'"[^"]*"'),       # String literals
        ('ID',       r'[A-Za-z_]\w*'),  # Identifiers
        ('ASSIGN',   r'='),             # Assignment operator
        ('OP',       r'[+\-*/]'),       # Arithmetic operators
        ('LPAREN',   r'\('),            # Left parenthesis
        ('RPAREN',   r'\)'),            # Right parenthesis
        ('NEWLINE',  r'\n'),            # Line endings
        ('SKIP',     r'[ \t]+'),        # Skip spaces and tabs
        ('COMMENT',  r'#.*'),           # Comments
        ('MISMATCH', r'.'),             # Any other character
    ]
    
    # Create a regular expression from token specifications
    token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
    
    # Scan through the source code
    for match in re.finditer(token_regex, source_code):
        kind = match.lastgroup
        value = match.group(kind)
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'STRING':
            value = value.strip('"')
        elif kind == 'ID':
            pass
        elif kind == 'ASSIGN':
            pass
        elif kind == 'OP':
            pass
        elif kind == 'LPAREN' or kind == 'RPAREN':
            pass
        elif kind == 'NEWLINE':
            pass
        elif kind == 'SKIP':
            continue
        elif kind == 'COMMENT':
            # Ignore comments
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character: {value}')
        tokens.append((kind, value))
    
    return tokens
