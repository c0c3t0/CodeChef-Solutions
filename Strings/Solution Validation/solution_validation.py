def validate(string):
    if 'def' not in string:
        return 'missing def'
    elif ':' not in string:
        return 'missing :'
    elif '(' and ')' not in string:
        return 'missing paren'
    elif '(' + ')' in string:
        return 'missing param'
    elif ' '*4 not in string:
        return 'missing indent'
    elif 'validate' not in string:
        return 'wrong name'
    elif 'return' not in string:
        return 'missing return'
    else:
        return True
