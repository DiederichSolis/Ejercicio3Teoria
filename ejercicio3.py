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
