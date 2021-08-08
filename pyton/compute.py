def compute(a,b,c):
    a = int(a)
    c = int(c)
    if b == "+":
        res = a + c
    if b == "-":
        res = a - c
    if b == "/":
        res = a / c
    if b == "*":
        res = a * c
    return res