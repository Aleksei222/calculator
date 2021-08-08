def tokenizator(str):
    array = []
    token = ""
    signs = "+()/*"
    for lit in str:
        length = len(array)
        if lit == "-":
            try:
                topToken = array[-1]
                if topToken != "(":
                    if token != '':
                        array.append(token)
                    token = ""
                    array.append(lit)
            except IndexError:
                pass
        if lit in signs:
            if token != '':
                array.append(token)
            token = ""
            array.append(lit)                                                                   
        if length == len(array):
            if lit == "-":
                if token == "":
                    token += lit
                else:
                    array.append(token)
                    token = ""
                    array.append(lit)
            else:    
                token += lit
    if token != '':
        array.append(token)
    return array