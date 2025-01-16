def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, 'sin': 4, 'cos': 4, 'log': 4, 'tg': 4, 'exp': 4}
    stack = []
    postfix = []
    flag = False
    i = 0
    while i < len(expression):
        char = expression[i]
        if char.isdigit():
            arr = ""
            flag = True
            while flag:
                if i < (len(expression) - 1):
                    tmp = expression[i + 1]
                if not tmp.isdigit():
                    flag = False
                    char = expression[i]
                    arr += char
                    i += 1
                    break
                char = expression[i]
                arr += char
                i += 1
            postfix.append(arr + ' ')
        elif char.isalpha():
            arr = ""
            flag = True
            if char == 'x':
                postfix.append(char + ' ')
                i += 1
            else:
                while flag:
                    if i < (len(expression) - 1):
                        tmp = expression[i + 1]
                    if not tmp.isalpha():
                        flag = False
                        char = expression[i]
                        arr += char
                        i += 1
                        break
                    char = expression[i]
                    arr += char
                    i += 1
                stack.append(arr)
        elif char == '(':
            stack.append(char)
            i += 1
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop() + ' ')
            stack.pop()
            i += 1
        else:
            while stack and precedence.get(stack[-1], 0) >= precedence.get(char, 0):
                postfix.append(stack.pop() + ' ')
            stack.append(char)
            i += 1
    while stack:
        postfix.append(stack.pop() + ' ')
    return ''.join(postfix)

file = open("infix.txt")
infix_expression = file.read()
file.close()
postfix_expression = infix_to_postfix(infix_expression)
print(postfix_expression)
out = open("rpn.txt", "w")
out.write(postfix_expression)
out.close()