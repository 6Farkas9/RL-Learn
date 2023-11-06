
def getWinner(borad):
    for i in range(0,3):
        if (borad[i] == borad[i+3] == borad[i+6]) and borad[i] != 0:
            return borad[i]
        if (borad[i * 3] == borad[i * 3 + 1] == borad[i * 3 + 2]) and borad[i * 3] != 0:
            return borad[i * 3]
    if ((borad[0] == borad[4] == borad[8]) or (borad[2] == borad[4] == borad[6])) and borad[4] != 0:
        return borad[4]
    return 0

def judgeIfWin(borad):
    for i in range(0,3):
        if (borad[i] == borad[i+3] == borad[i+6]) and borad[i] != 0:
            return True
        if (borad[i * 3] == borad[i * 3 + 1] == borad[i * 3 + 2]) and borad[i * 3] != 0:
            return True
    if ((borad[0] == borad[4] == borad[8]) or (borad[2] == borad[4] == borad[6])) and borad[4] != 0:
        return True
    return False

def chessToString(chess):
    stc = ''.join(list(map(lambda x:str(x),chess)))
    return stc

def stringToChess(string):
    chess = list(map(lambda x:int(x),string))
    return chess