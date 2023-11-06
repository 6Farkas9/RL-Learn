from tkinter import *
from tkinter.messagebox import *
from TrainModel import *

class MY_GUI():
    def __init__(self):
        self.state = finalresultInput()
        self.root = Tk()
        self.buttonlist = []
        for i in range(9):
            self.buttonlist.append(Button(command=lambda arg=i:self.button_Press_Event(arg),width=15, height=5))
            self.buttonlist[i].grid(row=int(i / 3), column=i % 3)
        self.reSet_Window()

    def set_Button_StateAndText(self):
        for i in range(9):
            if self.currentchess[i] == 1:
                self.buttonlist[i].config(text="X",state="disabled")
            elif self.currentchess[i] == 2:
                self.buttonlist[i].config(text="O", state="disabled")
            else:
                self.buttonlist[i].config(text="", state="normal")

    def pc_One_Step(self):
        posusable = getPositionUsable(self.currentchess)
        maxpos = posusable[0]
        maxvalue = -1
        for pos in posusable:
            chessmodif = self.currentchess.copy()
            chessmodif[pos] = 1
            value = self.state[chessToString(chessmodif)]
            if value > maxvalue:
                maxpos = pos
                maxvalue = value
        self.currentchess[maxpos] = 1
        self.set_Button_StateAndText()
        if judgeIfWin(self.currentchess):
            result = showinfo("可惜","傻逼，连电脑都赢不了")
            self.reSet_Window()
        elif len(getPositionUsable(self.currentchess)) == 0:
            result = showinfo("可惜", "平嘞")
            self.reSet_Window()
        else:
            self.currentplayer = 2

    def reSet_Window(self):
        self.currentplayer = randint(1, 2)
        self.currentchess = [0]*9
        self.set_Button_StateAndText()
        if self.currentplayer == 1:
            self.pc_One_Step()

    def window_show(self):
        self.root.mainloop()

    def button_Press_Event(self,n):
        # self.buttonlist[n].config(text="O",state="disabled")
        self.currentchess[n] = 2
        self.set_Button_StateAndText()
        if judgeIfWin(self.currentchess):
            result = showinfo("可以","竟然赢了")
            self.reSet_Window()
        elif len(getPositionUsable(self.currentchess)) == 0:
            result = showinfo("可惜", "平嘞")
            self.reSet_Window()
        else:
            self.currentplayer = 1
            self.pc_One_Step()
