def insideParentheses(s): return s.split('(', 1)[1].split(')')[0]

def getCharPos(input):
    tup = insideParentheses(input).split(',')
    return tup[0], int(tup[1])