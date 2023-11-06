from operator import *
from Tools import *

def generateState_byDelete():
    statechessall = [[a,b,c,d,e,f,g,h,i]
                for a in range(3) for b in range(3) for c in range(3)
                for d in range(3) for e in range(3) for f in range(3)
                for g in range(3) for h in range(3) for i in range(3)]
    stateall = []
    for item in statechessall:
        if abs(item.count(1) - item.count(2)) > 1:
            continue
        count = 0
        for i in range(0, 3):
            if item[i] == item[i + 3] and item[i + 3] == item[i + 6] and item[i] != 0:
                count += 1
                winp = item[i]
            if item[i * 3] == item[i * 3 + 1] and item[i * 3] == item[i * 3 + 2] and item[i * 3] != 0:
                count += 1
                winp = item[i * 3]
        if (item[0] == item[4] == item[8]) and item[4] != 0:
            count += 1
            winp = item[4]
        if (item[2] == item[4] == item[6]) and item[4] != 0:
            count += 1
            winp = item[4]
        if count > 1:
            continue
        if count == 1:
            if (winp == 1 and item.count(2) > item.count(1)) or (winp == 2 and item.count(1) > item.count(2)):
                continue
        stateall.append(item)
    return stateall

def generateState_byAdd():
    tempstateall = [[[[0,0,0,0,0,0,0,0,0]],[],[],[],[],[],[],[],[],[]],
                    [[[0,0,0,0,0,0,0,0,0]],[],[],[],[],[],[],[],[],[]]]
    for listnum in range(2):
        currentP = listnum + 1
        for i in range(9):
            infoToAppend = []
            for currentchess in tempstateall[listnum][i]:
                iswin = judgeIfWin(currentchess)
                if not iswin:
                    for j in range(9):
                        if currentchess[j] == 0:
                            chessToModif = currentchess.copy()
                            chessToModif[j] = currentP
                            if chessToModif not in infoToAppend:
                                infoToAppend.append(chessToModif.copy())
            tempstateall[listnum][i+1].extend(infoToAppend)
            if currentP == 1:
                currentP = 2
            else:
                currentP = 1
    stateall = []
    for i in range(10):
        for item in tempstateall[0][i]:
            if item in tempstateall[1][i]:
                tempstateall[0][i].remove(item)
        tempstateall[0][i].extend(tempstateall[1][i])
        stateall.extend(tempstateall[0][i].copy())
    return stateall

def generateStateData():
    finalstate = {}
    chessstate = generateState_byAdd()
    for chess in chessstate:
        if judgeIfWin(chess) and getWinner(chess) == 1:
            finalstate[chessToString(chess)] = 1
        elif judgeIfWin(chess) and getWinner(chess) == 2:
            finalstate[chessToString(chess)] = -1
        elif chess.count(0) == 0:
            finalstate[chessToString(chess)] = 0
        else:
            finalstate[chessToString(chess)] = 0
    return finalstate