def compute(a,b,c):
    try: 
        a = int(a)
    except ValueError:
        a = float(a)
    try:
        c = int(c)
    except ValueError:
        c = float(c)
    if b == "+":
        res = a + c
    if b == "-":
        res = a - c
    if b == "/":
        res = a / c
    if b == "*":
        res = a * c
    return res