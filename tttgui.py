from tkinter import *

class tttCanvas:
    def __init__(self):
        self.window = Tk()
        self.window.title('Tic Tac Toe')
        self.canvas_width = 300
        self.canvas_height = 320
        self.turn = 0  # if even, cross's turn, if odd, naught's turn
        self.winCondition = False

        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]


        # photoimage objects
        self.crossImg = PhotoImage(file="cross.png")
        self.naughtImg = PhotoImage(file="naught.png")

        frame = Frame(self.window)
        frame.pack()
        self.canvas = Canvas(frame, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()
        self.drawGrid()

        # bind mouse
        self.canvas.bind("<Button-1>", self.processMove)

        self.window.mainloop()


    def drawGrid(self):
        line2 = self.canvas.create_line(200, 10, 200, 290, width="3", tags='line2')
        line3 = self.canvas.create_line(10, 100, 290, 100, width="3", tags='line3')
        line4 = self.canvas.create_line(10, 200, 290, 200, width="3", tags='line4')
        line1 = self.canvas.create_line(100, 10, 100, 290, width="3", tags="line1")


    def processTurn(self):
        if self.turn % 2 == 0:
            return 'x'
        else:
            return 'o'

    def processVictoryCondition(self):
        # Horizontal wins
        for i in range(3):
            if self.board[i] == ['x','x','x']:
                self.canvas.create_text(150, 310, text="X Wins!!", tags='winner')
                self.winCondition = True
            if self.board[i] == ['o','o','o']:
                self.canvas.create_text(150, 310, text="O Wins!!", tags='winner')
                self.winCondition = True

        # Vertical wins
        for j in range(3):
            column = []
            for i in range(3):
                if self.board[i][j] != ' ':
                    column.append(self.board[i][j])
            if column == ['x','x','x']:
                self.canvas.create_text(150, 310, text="X Wins!!", tags='winner')
                self.winCondition = True
            if column == ['o','o','o']:
                self.canvas.create_text(150, 310, text="O Wins!!", tags='winner')
                self.winCondition = True

        # Diagonal wins
        diagonal = []
        for i in range(3):
            for j in range(3):
                if i == j and self.board[i][j] != ' ':
                    diagonal.append(self.board[i][j])
            if diagonal == ['x','x','x']:
                self.canvas.create_text(150, 310, text="X Wins!!", tags='winner')
                self.winCondition = True
            if diagonal == ['o','o','o']:
                self.canvas.create_text(150, 310, text="O Wins!!", tags='winner')
                self.winCondition = True

        oppositeDiagonal = []
        for i in range(3):
            oppositeDiagonal.append(self.board[i][2-i])
        if oppositeDiagonal == ['x', 'x', 'x']:
            self.canvas.create_text(150, 310, text="X Wins!!", tags='winner')
            self.winCondition = True
        if oppositeDiagonal == ['o', 'o', 'o']:
            self.canvas.create_text(150, 310, text="O Wins!!", tags='winner')
            self.winCondition = True



    def resetBoard(self):
        self.canvas.delete('cross')
        self.canvas.delete('naught')
        # TODO attach to button


    def processMove(self, event):
        player = self.processTurn()
        if player == 'x' and self.winCondition == False:
            for i in range(3):
                for j in range(3):
                    if j*100 < event.x < (j + 1)*100 and i*100 < event.y < (i+1)*100 and self.board[i][j] == ' ':
                        self.canvas.create_image((j*100)+50, (i*100)+50, image=self.crossImg, tags='cross')
                        self.turn += 1
                        self.board[i][j] = 'x'
                        self.processVictoryCondition()
        if player == 'o' and self.winCondition == False:
            for i in range(3):
                for j in range(3):
                    if j*100 < event.x < (j + 1)*100 and i*100 < event.y < (i+1)*100 and self.board[i][j] == ' ':
                        self.canvas.create_image((j*100)+50, (i*100)+50, image=self.naughtImg, tags='naught')
                        self.turn += 1
                        self.board[i][j] = 'o'
                        self.processVictoryCondition()


tttCanvas()