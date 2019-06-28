"""
Code illustration: 4.02
#no changes

tkinter GUI Application Development Hotshot
""" 

from tkinter import *
import chessboard


class GUI(dict):
    rows = 8
    columns = 8
    color1 = "#DDB88C"
    color2 = "#A66D4F"
    dim_square = 64
    images = {}

    def __init__(self, parent, chessboard):
        self.parent = parent
        self.chessboard = chessboard
        canvas_width = self.columns * self.dim_square
        canvas_height = self.rows * self.dim_square
        self.canvas = Canvas(parent, width=canvas_width, height=canvas_height)
        self.canvas.pack(padx=8, pady=8)
        self.draw_board()
  
    def draw_board(self):
        color = self.color2
        for r in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for c in range(self.columns):
                x1 = (c * self.dim_square)
                y1 = ((7-r) * self.dim_square)
                x2 = x1 + self.dim_square
                y2 = y1 + self.dim_square
                self.canvas.create_rectangle(x1, y1, x2, y2,  fill=color, tags="board")
                color = self.color1 if color == self.color2 else self.color2

        
def main(chessboard):
    root = Tk()
    root.title("Chess")
    gui = GUI(root, chessboard)
    gui.draw_board()
    root.mainloop()

if __name__ == "__main__":
    game = chessboard.Board()
    main(game)
    
