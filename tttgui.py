from tkinter import *

class tttCanvas:
    def __init__(self):
        self.window = Tk()
        self.window.title('Tic Tac Toe')
        self.canvas_width = 300
        self.canvas_height = 300
        self.turn = 0  # if even, cross's turn, if odd, naught's turn
        self.winCondition = False

        self.board = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
                      'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
                      'low-l': ' ', 'low-m': ' ', 'low-r': ' '}


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
        # this will work better with a nested list
        # the positions on the board need numerical relations to one another
        # in order to implement this kind of logic
        return None


    def processMove(self, event):
        player = self.processTurn()
        if player == 'x' and self.winCondition == False:
            if 0 < event.x < 100 and 0 < event.y < 100 and self.board['top-l'] == ' ':
                self.canvas.create_image(50, 50, image = self.crossImg)
                self.turn += 1
                move = 'top-l'
                self.board[move] = player
            if 100 < event.x < 200 and 0 < event.y < 100 and self.board['top-m'] == ' ':
                self.canvas.create_image(150, 50, image=self.crossImg)
                self.turn += 1
                move = 'top-m'
                self.board[move] = player
            if 200 < event.x < 300 and 0 < event.y < 100 and self.board['top-r'] == ' ':
                self.canvas.create_image(250, 50, image=self.crossImg)
                self.turn += 1
                move = 'top-r'
                self.board[move] = player
            if 0 < event.x < 100 and 100 < event.y < 200 and self.board['mid-l'] == ' ':
                self.canvas.create_image(50, 150, image = self.crossImg)
                self.turn += 1
                move = 'mid-l'
                self.board[move] = player
            if 100 < event.x < 200 and 100 < event.y < 200 and self.board['mid-m'] == ' ':
                self.canvas.create_image(150, 150, image=self.crossImg)
                self.turn += 1
                move = 'mid-m'
                self.board[move] = player
            if 200 < event.x < 300 and 100 < event.y < 200 and self.board['mid-r'] == ' ':
                self.canvas.create_image(250, 150, image=self.crossImg)
                self.turn += 1
                move = 'mid-r'
                self.board[move] = player
            if 0 < event.x < 100 and 200 < event.y < 300 and self.board['low-l'] == ' ':
                self.canvas.create_image(50, 250, image=self.crossImg)
                self.turn += 1
                move = 'low-l'
                self.board[move] = player
            if 100 < event.x < 200 and 200 < event.y < 300 and self.board['low-m'] == ' ':
                self.canvas.create_image(150, 250, image=self.crossImg)
                self.turn += 1
                move = 'low-m'
                self.board[move] = player
            if 200 < event.x < 300 and 200 < event.y < 300 and self.board['low-r'] == ' ':
                self.canvas.create_image(250, 250, image=self.crossImg)
                self.turn += 1
                move = 'low-r'
                self.board[move] = player
            # create a nested loop that does this
        if player == 'o' and self.winCondition == False:
            if 0 < event.x < 100 and 0 < event.y < 100 and self.board['top-l'] == ' ':
                self.canvas.create_image(50, 50, image = self.naughtImg)
                self.turn += 1
                move = 'top-l'
                self.board[move] = player
            if 100 < event.x < 200 and 0 < event.y < 100 and self.board['top-m'] == ' ':
                self.canvas.create_image(150, 50, image=self.naughtImg)
                self.turn += 1
                move = 'top-m'
                self.board[move] = player
            if 200 < event.x < 300 and 0 < event.y < 100 and self.board['top-r'] == ' ':
                self.canvas.create_image(250, 50, image=self.naughtImg)
                self.turn += 1
                move = 'top-r'
                self.board[move] = player
            if 0 < event.x < 100 and 100 < event.y < 200 and self.board['mid-l'] == ' ':
                self.canvas.create_image(50, 150, image = self.naughtImg)
                self.turn += 1
                move = 'mid-l'
                self.board[move] = player
            if 100 < event.x < 200 and 100 < event.y < 200 and self.board['mid-m'] == ' ':
                self.canvas.create_image(150, 150, image=self.naughtImg)
                self.turn += 1
                move = 'mid-m'
                self.board[move] = player
            if 200 < event.x < 300 and 100 < event.y < 200 and self.board['mid-r'] == ' ':
                self.canvas.create_image(250, 150, image=self.naughtImg)
                self.turn += 1
                move = 'mid-r'
                self.board[move] = player
            if 0 < event.x < 100 and 200 < event.y < 300 and self.board['low-l'] == ' ':
                self.canvas.create_image(50, 250, image=self.naughtImg)
                self.turn += 1
                move = 'low-l'
                self.board[move] = player
            if 100 < event.x < 200 and 200 < event.y < 300 and self.board['low-m'] == ' ':
                self.canvas.create_image(150, 250, image=self.naughtImg)
                self.turn += 1
                move = 'low-m'
                self.board[move] = player
            if 200 < event.x < 300 and 200 < event.y < 300 and self.board['low-r'] == ' ':
                self.canvas.create_image(250, 250, image=self.naughtImg)
                self.turn += 1
                move = 'low-r'
                self.board[move] = player


tttCanvas()