# FSM to recognize decimal, octal, and hexadecimal integer literals
class IntegerFSM:
    def __init__(self):
        self.current_state = 'start'
        self.valid_states = {'integer', 'octal_integer', 'hexadecimal_integer'}
        self.transitions = {
            'start': {'digit': 'integer', '0': 'octal_prefix', '-': 'negative_sign'},
            'negative_sign': {'digit': 'integer'},
            'integer': {'digit': 'integer'},
            'octal_prefix': {'digit': 'octal_integer', 'o': 'octal_integer', 'O': 'octal_integer'},
            'octal_integer': {'digit': 'octal_integer'},
            'hexadecimal_prefix': {'digit': 'hexadecimal_integer', 'a': 'hexadecimal_integer', 'A': 'hexadecimal_integer', 'b': 'hexadecimal_integer', 'B': 'hexadecimal_integer', 'c': 'hexadecimal_integer', 'C': 'hexadecimal_integer', 'd': 'hexadecimal_integer', 'D': 'hexadecimal_integer', 'e': 'hexadecimal_integer', 'E': 'hexadecimal_integer', 'f': 'hexadecimal_integer', 'F': 'hexadecimal_integer'},
            'hexadecimal_integer': {'digit': 'hexadecimal_integer'}
        }

    def process(self, input_string):
        for char in input_string:
            if char.isdigit():
                self.current_state = self.transitions[self.current_state]['digit']
            elif char == '0':
                if self.current_state == 'start':
                    self.current_state = 'octal_prefix'
                elif self.current_state == 'hexadecimal_prefix':
                    self.current_state = 'hexadecimal_integer'
                else:
                    self.current_state = 'invalid'
            elif char == 'o' or char == 'O':
                if self.current_state == 'octal_prefix':
                    self.current_state = 'octal_integer'
                else:
                    self.current_state = 'invalid'
            elif char == 'x' or char == 'X':
                if self.current_state == 'start':
                    self.current_state = 'hexadecimal_prefix'
                else:
                    self.current_state = 'invalid'
            elif char == '-':
                if self.current_state == 'start':
                    self.current_state = 'negative_sign'
                else:
                    self.current_state = 'invalid'
            else:
                self.current_state = 'invalid'
            
            if self.current_state == 'invalid':
                return False
        
        return self.current_state in self.valid_states


# Main program
while True:
    input_string = input('Enter an integer: ')

    if input_string == 'q':
        break

    fsm = IntegerFSM()

    if fsm.process(input_string):
        print(f'{input_string} is a valid integer')
    else:
        print(f'{input_string} is not a valid integer')
