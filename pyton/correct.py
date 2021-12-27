import re

def co(str):
    a = 0
    b1 = 0
    b2 = 0
    for lit in str:
        if lit == "(":
            b1 += 1
            a += 1
        if lit == ")":
            b2 += 1
            if a == 0:
                return True
            else:
                a -= 1
        if a < 0:
            return True
    if b1 != b2:
        return True
    return False

def ex(str):
    alg = "+/-*"
    num = '1234567890'
    alg_met = 0
    num_met = 0
    for lit in str:
        if lit in alg:
            alg_met+=1
        if lit in num:
            num_met+=1
    if alg_met==0 or num_met==0:
        return True
    return False

def inc(str):
    reg1 = re.compile(r'\([+/*]')
    reg2 = re.compile(r'[-+*/]\)')
    reg3 = re.compile(r'\d\(')
    reg4 = re.compile(r'\)\d')
    reg5 = re.compile(r'[+/*]')
    reg6 = re.compile(r'[-+/*]{2}')
    reg7 = re.compile(r'/0')
    if reg1.search(str)!=None or reg2.search(str)!=None or reg3.search(str)!=None or reg4.search(str)!=None or reg5.match(str)!=None or reg6.search(str)!=None or reg7.search(str)!=None:
        return True
    return False

def correct(str):
    a = "+-/*1234567890()."
    for lit in str:
        if lit not in a:
            return False
        else:
            continue
    if co(str):
        return False
    if ex(str):
        return False
    if inc(str):
        return False
    return True
