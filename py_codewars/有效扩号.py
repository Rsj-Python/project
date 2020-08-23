def valid_parentheses(string):
    a = 0
    for i in string:
        if i == '(':
            a += 1
        if i == ')':
            a -= 1
            if a < 0:
                return a
    return a == 0
print(valid_parentheses('())((())()'))

























