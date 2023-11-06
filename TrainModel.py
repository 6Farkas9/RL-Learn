# V(S) = V(s) + a[V(s1) - V(s)]
# V(S)为待电脑下的状态，V(S1)为电脑下完后的状态，即1等于2或者1多于2
# 贪心根据的是S1的胜率之间的比较，这样无需考虑人怎么下的（大概）
# 电脑永远下1

from random import *
from Tools import *
from FileIO import *

theta = 0.05 # 试探非贪心大小
state = {}
alpha = 0.1

# 获取当前棋盘的可下棋位置
def getPositionUsable(chess):
    res = []
    for i in range(9):
        if chess[i] == 0:
            res.append(i)
    return res

# 按照theta贪心策略选择当下的动作
def getGreedyActionByTheta(chess):
    posusable = getPositionUsable(chess)
    maxpos = posusable[0]
    maxvalue = -1
    for pos in posusable:
        chessmodif = chess.copy()
        chessmodif[pos] = 1
        key_chess = chessToString(chessmodif)
        if state[key_chess] > maxvalue:
            maxpos = pos
            maxvalue = state[key_chess]
    randnum = randint(1,100)
    if randnum > 100 * theta:
        return maxpos
    else:
        return choice(posusable)

def getGreedyAction(chess):
    for i in range(9):
        if chess[i] == 1:
            chess[i] = 2
        elif chess[i] == 2:
            chess[i] = 1
    posusable = getPositionUsable(chess)
    maxpos = posusable[0]
    maxvalue = -1
    for pos in posusable:
        chessmodif = chess.copy()
        chessmodif[pos] = 1
        key_chess = chessToString(chessmodif)
        if state[key_chess] > maxvalue:
            maxpos = pos
            maxvalue = state[key_chess]
    for i in range(9):
        if chess[i] == 1:
            chess[i] = 2
        elif chess[i] == 2:
            chess[i] = 1
    return maxpos

def train(alpha_l = 0.1,theta_l = 0.05,state_l = {},times = 1e+5):
    global alpha,theta,state
    alpha = alpha_l
    theta = theta_l
    state = state_l.copy()
    for i in range(times):
        currentplayer = randint(1, 2)
        currentchess = [0,0,0,0,0,0,0,0,0]
        statepassby = []
        while True:
            if currentplayer == 1:
                pos = getGreedyActionByTheta(currentchess)
                currentchess[pos] = 1
                statepassby.append(chessToString(currentchess))
            else:
                pos = getGreedyAction(currentchess)
                currentchess[pos] = 2
            if judgeIfWin(currentchess) or len(getPositionUsable(currentchess)) == 0:
                if currentplayer == 2:
                    statepassby.append(chessToString(currentchess))
                i = len(statepassby) - 2
                while i >= 0:
                    state[statepassby[i]] = state[statepassby[i]] + alpha * (state[statepassby[i+1]] - state[statepassby[i]])
                    i -= 1
                break
            if currentplayer == 1:
                currentplayer = 2
            else:
                currentplayer = 1
    finalResultOutput(state)


