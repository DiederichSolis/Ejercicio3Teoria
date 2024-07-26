def get_precedence(c):
    precedence = {
        '(': 1,
        '|': 2,
        '.': 3,
        '?': 4,
        '*': 4,
        '+': 4,
        '^': 5
    }
    return precedence.get(c, 6)  

def format_regex(regex):
    all_operators = ['|', '?', '+', '*', '^']
    binary_operators = ['^', '|']
    res = ""
    
    i = 0
    while i < len(regex):
        c1 = regex[i]
        if i + 1 < len(regex):
            c2 = regex[i + 1]
            res += c1
            if (c1 != '(' and c2 != ')' and c2 not in all_operators and c1 not in binary_operators):
                res += '.'
        i += 1
    res += regex[-1]
    
    return res

def infix_to_postfix(regex):
    postfix = ""
    stack = []
    formatted_regex = format_regex(regex)
    steps = []

    for c in formatted_regex:
        if c.isalnum() or c == 'ε':
            postfix += c
            steps.append(f"Added '{c}' to postfix expression")
        elif c == '(':
            stack.append(c)
            steps.append(f"Pushed '{c}' to stack")
        elif c == ')':
            while stack and stack[-1] != '(':
                top = stack.pop()
                postfix += top
                steps.append(f"Popped '{top}' from stack to postfix expression")
            stack.pop()  # Remove '(' from stack
            steps.append(f"Popped '(' from stack")
        else:
            while stack and get_precedence(stack[-1]) >= get_precedence(c):
                top = stack.pop()
                postfix += top
                steps.append(f"Popped '{top}' from stack to postfix expression")
            stack.append(c)
            steps.append(f"Pushed '{c}' to stack")

    while stack:
        top = stack.pop()
        postfix += top
        steps.append(f"Popped '{top}' from stack to postfix expression")
    
    return postfix, steps

def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            regex = line.strip()
            if not regex:
                continue
            postfix, steps = infix_to_postfix(regex)
            outfile.write(f"Original: {regex}\n")
            outfile.write(f"Postfix: {postfix}\n")
            outfile.write("Steps:\n")
            for step in steps:
                outfile.write(f"{step}\n")
            outfile.write("\n")

# Archivo de entrada y salida
input_file = 'input_regex.txt'
output_file = 'output_postfix.txt'

# Procesar el archivo
process_file(input_file, output_file)
