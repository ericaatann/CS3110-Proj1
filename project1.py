def parse_expression(input_str):
    """Parses the input string and returns a tuple of two numbers and an operator."""
    tokens = input_str.split()
    if len(tokens) != 3:
        return None
    operand1 = parse_number(tokens[0])
    operand2 = parse_number(tokens[2])
    if operand1 is None or operand2 is None:
        return None
    if tokens[1] not in ['+', '-', '*', '/']:
        return None
    return operand1, operand2, tokens[1]

def parse_number(token):
    """Parses a number from the input token."""
    if token.startswith('0x') or token.startswith('0X'):
        return parse_hex(token[2:])
    elif token.startswith('0o') or token.startswith('0O'):
        return parse_oct(token[2:])
    else:
        return parse_dec(token)

def parse_hex(token):
    """Parses a hexadecimal integer from the input token."""
    value = 0
    for c in token:
        if c.isdigit():
            value = value * 16 + int(c)
        elif c in ['a', 'A']:
            value = value * 16 + 10
        elif c in ['b', 'B']:
            value = value * 16 + 11
        elif c in ['c', 'C']:
            value = value * 16 + 12
        elif c in ['d', 'D']:
            value = value * 16 + 13
        elif c in ['e', 'E']:
            value = value * 16 + 14
        elif c in ['f', 'F']:
            value = value * 16 + 15
        else:
            return None
    return value

def parse_oct(token):
    """Parses an octal integer from the input token."""
    value = 0
    for c in token:
        if c in ['0', '1', '2', '3', '4', '5', '6', '7']:
            value = value * 8 + int(c)
        else:
            return None
    return value

def parse_dec(token):
    """Parses a decimal integer from the input token."""
    if not token.isdigit():
        return None
    return int(token)

while True:
    input_str = input('Enter an expression (e.g. 2 + 3): ').strip()

    if len(input_str) > 20:
        print('Input too long. Please enter an expression with at most 20 characters.')
        continue

    expr = parse_expression(input_str)
    if expr is None:
        print('Invalid input. Please enter a valid expression (e.g. 2 + 3).')
        continue

    operand1, operand2, operator = expr
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        if operand2 == 0:
            print('Error: division by zero.')
            continue
        result = operand1 / operand2
    else:
        result = None

    if result is not None:
        print('Result:', result)
    else:
        print('Unknown operator.')