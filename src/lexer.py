import re

def tokenize(source_code):
    tokens = []
    
    token_specification = [
        ('NUMBER',   r'\d+(\.\d*)?'),
        ('STRING',   r'"[^"]*"'),
        ('ID',       r'[A-Za-z_]\w*'),
        ('ASSIGN',   r'='),
        ('OP',       r'[+\-*/]'),
        ('COMPARE',  r'[<>!=]=?|=='),
        ('LPAREN',   r'\('),
        ('RPAREN',   r'\)'),
        ('NEWLINE',  r'\n'),
        ('SKIP',     r'[ \t]+'),
        ('COMMENT',  r'#.*'),
        ('MISMATCH', r'.'),
    ]
    
    token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
    
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
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character: {value}')
        tokens.append((kind, value))
    
    return tokens
