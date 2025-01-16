import math as m

def toInfix(rpn_string: str):
    stack = []
    func = ''
    for token in rpn_string.split():
        if token == '+':
            a = (stack.pop());
            b = stack.pop();
            tmp = '(' + b + ' + ' + a + ')'
            stack.append(tmp)
        elif token == '-':
            a = stack.pop();
            b = stack.pop();
            tmp = '(' + b + ' - ' + a + ')'
            stack.append(tmp)
        elif token == '/':
            a = stack.pop();
            b = stack.pop();
            tmp = b + ' / ' + a
            stack.append(tmp)
        elif token == '*':
            a = stack.pop();
            b = stack.pop();
            tmp = b + ' * ' + a
            stack.append(tmp)
        elif token == '^':
            a = stack.pop();
            b = stack.pop();
            tmp = b + ' ** ' + a
            stack.append(tmp)
        elif token == 'exp':
            a = stack.pop();
            tmp = 'exp(' + a + ')'
            stack.append(tmp)
        elif token == 'log':
            a = stack.pop();
            tmp = 'log(' + a + ')'
            stack.append(tmp)
        elif token == 'sqrt':
            a = stack.pop();
            tmp = 'sqrt(' + a + ')'
            stack.append(tmp)
        elif token == 'cos':
            a = stack.pop();
            tmp = 'cos(' + a + ')'
            stack.append(tmp)
        elif token == 'sin':
            a = stack.pop();
            tmp = 'sin(' + a + ')'
            stack.append(tmp)
        elif token == 'tan':
            a = stack.pop();
            tmp = 'tan(' + a + ')'
            stack.append(tmp)
        elif token == 'pi':
            a = stack.pop();
            b = stack.pop();
            tmp = 'pi'
            stack.append(tmp)
        else:
            try:
                stack.append(token)
            except ValueError:
                raise ValueError(f"{token!r} - неизвестная операция")
    return stack.pop()

def func(rpn_string: str, valueX: int):
    stack = []
    func = ''
    for token in rpn_string.split():
        if token == 'x':
            stack.append(valueX)
        elif token == '+':
            a = stack.pop();
            b = stack.pop();
            tmp = b + a
            stack.append(tmp)
        elif token == '-':
            a = stack.pop();
            b = stack.pop();
            tmp = b - a
            stack.append(tmp)
        elif token == '/':
            a = stack.pop();
            b = stack.pop();
            tmp = b / a
            stack.append(tmp)
        elif token == '*':
            a = stack.pop();
            b = stack.pop();
            tmp = b * a
            stack.append(tmp)
        elif token == '^':
            a = stack.pop();
            b = stack.pop();
            tmp = b ** a
            stack.append(tmp)
        elif token == 'exp':
            a = stack.pop();
            tmp = m.exp(a)
            stack.append(tmp)
        elif token == 'log':
            a = stack.pop();
            tmp = m.log(a)
            stack.append(tmp)
        elif token == 'sqrt':
            a = stack.pop();
            tmp = m.sqrt(a)
            stack.append(tmp)
        elif token == 'cos':
            a = stack.pop();
            tmp = m.cos(a)
            stack.append(tmp)
        elif token == 'sin':
            a = stack.pop();
            tmp = m.sin(a)
            stack.append(tmp)
        elif token == 'tan':
            a = stack.pop();
            tmp = m.tan(a)
            stack.append(tmp)
        elif token == 'pi':
            a = stack.pop();
            b = stack.pop();
            tmp = m.pi
            stack.append(tmp)
        else:
            try:
                stack.append(int(token))
            except ValueError:
                raise ValueError(f"{token!r} - неизвестная операция")
    return stack.pop()

def f(x: int):
    return (3 + 2 * (1 - x) ** 2)

def work(f, a, b, n, tmp: str, out):
    print("\nЧисло разбиений: ", n)
    out.write("Число разбиений: " + str(n))
    h = (b-a)/float(n)
    print("Шаг:", h)
    out.write("\nШаг:" + str(h))
    total = sum([f(tmp, a + (k*h)) for k in range(0, n)])
    result = h * total
    print("Результат: ", result)
    out.write("\nРезультат: " + str(result))
    return result


file = open('rpn.txt')
tmp = file.read()
res = toInfix(tmp)
print(res)
file.close()
with open("param.txt") as file:
    for line in file:
        a, b, n = line.split()
out = open("res.txt", "w")
work(func, int(a), int(b), int(n), tmp, out)
out.close()