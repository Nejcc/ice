class ASTNode:
    def __init__(self, node_type, value=None, children=None):
        self.node_type = node_type
        self.value = value
        self.children = children or []

    def __repr__(self):
        return f"{self.node_type}: {self.value} -> {self.children}"

def parse(tokens):
    def expect(expected_type):
        if tokens and tokens[0][0] == expected_type:
            return tokens.pop(0)
        else:
            raise SyntaxError(f"Expected {expected_type} but found {tokens[0][0]}")

    def parse_expression():
        left = parse_term()

        while tokens and tokens[0][0] == 'OP':
            op_token = tokens.pop(0)
            right = parse_term()
            left = ASTNode('Operation', op_token[1], [left, right])

        return left

    def parse_term():
        if tokens[0][0] == 'NUMBER':
            return ASTNode('Number', expect('NUMBER')[1])
        elif tokens[0][0] == 'ID':
            return ASTNode('Variable', expect('ID')[1])
        else:
            raise SyntaxError(f"Unexpected token: {tokens[0][0]}")

    def parse_condition():
        left = parse_term()
        if tokens and tokens[0][0] == 'COMPARE':
            comp_token = tokens.pop(0)
            right = parse_term()
            return ASTNode('Condition', comp_token[1], [left, right])
        else:
            raise SyntaxError(f"Expected comparison operator but found {tokens[0][0]}")

    ast = ASTNode("Program")
    while tokens:
        token_type, token_value = tokens[0]

        if token_type == 'ID' and token_value == 'if':
            tokens.pop(0)
            expect('LPAREN')
            condition = parse_condition()
            expect('RPAREN')

            if_block = ASTNode('If', None, [condition])
            if tokens[0][0] == 'ID' or tokens[0][0] == 'STRING':
                if tokens[0][0] == 'ID' and tokens[0][1] == 'print':
                    tokens.pop(0)
                    expect('LPAREN')
                    if tokens[0][0] == 'STRING':
                        string_token = expect('STRING')
                        if_block.children.append(ASTNode('Print', string_token[1]))
                    elif tokens[0][0] == 'ID':
                        id_token = expect('ID')
                        if_block.children.append(ASTNode('PrintVar', id_token[1]))
                    else:
                        raise SyntaxError(f"Expected STRING or ID but found {tokens[0][0]}")
                    expect('RPAREN')
                else:
                    statement = parse_expression()
                    if_block.children.append(statement)

            ast.children.append(if_block)

        elif token_type == 'ID' and token_value == 'print':
            tokens.pop(0)
            expect('LPAREN')
            if tokens[0][0] == 'STRING':
                string_token = expect('STRING')
                ast.children.append(ASTNode('Print', string_token[1]))
            elif tokens[0][0] == 'ID':
                id_token = expect('ID')
                ast.children.append(ASTNode('PrintVar', id_token[1]))
            else:
                raise SyntaxError(f"Expected STRING or ID but found {tokens[0][0]}")
            expect('RPAREN')

        elif token_type == 'ID':
            id_token = tokens.pop(0)
            expect('ASSIGN')
            value_expression = parse_expression()
            ast.children.append(ASTNode('Assign', id_token[1], [value_expression]))

        elif token_type == 'NEWLINE':
            tokens.pop(0)
        else:
            raise SyntaxError(f"Unexpected token: {token_type}")

    return ast
