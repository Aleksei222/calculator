from pyton.stack import Stack
from pyton.tokenizator import tokenizator
from pyton.compute import compute


def calc(st):
    tokens = tokenizator(st)
            # break
    numbers = Stack()
    operators = Stack()
    for i in tokens:
        if i in "+-/*()":
            if i == ")":
                token = operators.getTop()
                operators.pop()
                while token!="(":
                    a = numbers.getTop()
                    numbers.pop()
                    b = numbers.getTop()
                    numbers.pop()
                    numbers.push(compute(b, token, a))
                    token = operators.getTop()
                    operators.pop()
            if i in "+-/*":
                try:
                    token = operators.getTop()
                    if token != "(":
                        if token in "*/" or i in "+-":
                            operators.pop()
                            a = numbers.getTop()
                            numbers.pop()
                            b = numbers.getTop()
                            numbers.pop()
                            numbers.push(compute(b, token, a))
                    operators.push(i)
                except IndexError:
                    operators.push(i)    
            if i == "(":
                operators.push(i)
        else:
            numbers.push(i)
    while numbers.length != 1:
        token = operators.getTop()
        operators.pop()
        a = numbers.getTop()
        numbers.pop()
        b = numbers.getTop()
        numbers.pop()
        numbers.push(compute(b, token, a))
    return str(numbers.getTop())
