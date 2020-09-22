def ColorText(text, color):
    CEND = '\033[0m'
    CBOLD = '\033[1m'
    CBLACK = '\033[30m'
    CRED = '\033[31m'
    CGREEN = '\033[32m'
    CYELLOW = '\033[33m'
    CBLUE = '\033[34m'
    CMAGENTA = '\033[35m'
    CCYAN = '\033[36m'
    CWHITE = '\033[37m'
    CRESET = '\033[39m'
    if color == 'black':
        return CBLACK + CBOLD + text + CEND
    if color == 'red':
        return CRED + CBOLD + text + CEND
    elif color == 'green':
        return CGREEN + CBOLD + text + CEND
    elif color == 'yellow':
        return CYELLOW + CBOLD + text + CEND
    elif color == 'blue':
        return CBLUE + CBOLD + text + CEND
    elif color == 'magenta':
        return CMAGENTA + CBOLD + text + CEND
    elif color == 'cyan':
        return CCYAN + CBOLD + text + CEND
    elif color == 'white':
        return CWHITE + CBOLD + text + CEND

    else:
        return CBOLD + text + CEND


