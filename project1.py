def parse_expression(input_str):
    """Parses the input string and returns a tuple of two numbers and an operator."""
    input_str.replace("_", "")
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
    if len(token) > 2 and token[0] == '0' and token[1] in ['x', 'X']:
        return parse_hex(token[2:])
    elif len(token) > 2 and token[0] == '0' and token[1] in ['o', 'O']:
        return parse_oct(token[2:])
    elif len(token) > 2 and token[0] == '0' and token[1] in ['b', 'B']:
        return parse_bin(token[2:])
    else:
        return parse_dec(token)

    
def parse_hex(token):
    """Parses a hexadecimal integer from the input token."""
    value = 0
    for c in token:
        if '0' <= c <= '9':
            value = value * 16 + int(c)
        elif 'a' <= c <= 'f' or 'A' <= c <= 'F':
            value = value * 16 + ord(c) - ord('a') + 10
        else:
            return None
    return value


def parse_oct(token):
    """Parses an octal integer from the input token."""
    value = 0
    for c in token:
        if '0' <= c <= '7':
            value = value * 8 + int(c)
        else:
            return None
    return value


def parse_bin(token):
    value = 0
    power = -1
    for c in token[::-1]:
        power += 1
        if c == "0":
            pass
        elif c == "1":
            value += 2**power * 1
        else:
            return None
    return value


def parse_dec(token):
    """Parses a decimal integer from the input token."""
    for c in token:
        if not '0' <= c <= '9':
            return None
    return int(token)


def main():
    """Main function"""
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


"""Runs main() function"""
if __name__ == '__main__':
    main()

