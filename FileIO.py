import json

def chessFileRead():
    with open("chess.json", 'r' ,encoding='utf-8') as read_f:
        load_f = read_f.read()
        load_f = json.loads(load_f)
    return load_f

def chessFileWriteOne(data):
    data_old = chessFileRead()
    data_old.append(data)
    with open("chess.json", 'w' ,encoding='utf-8') as write_f:
        json.dump(data_old,write_f,ensure_ascii=False)

def chessFileWriteAll(data):
    data_old = chessFileRead()
    data_old.extend(data)
    with open("chess.json", 'w' ,encoding='utf-8') as write_f:
        json.dump(data_old,write_f,ensure_ascii=False)

def finalResultOutput(state):
    with open("state.json", 'w' ,encoding='utf-8') as write_f:
        json.dump(state,write_f,ensure_ascii=False)

def finalresultInput():
    with open("state.json", 'r', encoding='utf-8') as read_f:
        load_f = read_f.read()
        load_f = json.loads(load_f)
    return load_f