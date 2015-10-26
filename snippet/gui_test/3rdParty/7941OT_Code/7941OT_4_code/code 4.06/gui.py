"""
Code illustration: 4.06


ATTRIBUTES ADDED
pieces = {}
selected = None
selected_piece = None
focused = None


METHOD MODFIED
Class GUI
__init__ (click event added)
draw_board modified to handle clicks

NEW METHODS ADDED
sqaureclicked
shift
focus


Tkinter GUI Application Development Hotshot
""" 
import chessboard
import pieces
from Tkinter import *
from PIL import ImageTk

class GUI():
    pieces = {}
    selected_piece = None
    focused = None
    images = {}
    color1 = "#DDB88C"
    color2 = "#A66D4F"
    highlightcolor ="khaki"
    rows = 8
    columns = 8
    dim_square = 64

    def __init__(self, parent, chessboard):
        self.chessboard = chessboard
        self.parent = parent
        canvas_width = self.columns * self.dim_square
        canvas_height = self.rows * self.dim_square
        self.canvas = Canvas(parent, width=canvas_width, height=canvas_height)
        self.canvas.pack(padx=8, pady=8)
        self.draw_board()
        self.canvas.bind("<Button-1>", self.square_clicked)



    def square_clicked(self, event):
        col_size = row_size = self.dim_square
        selected_column = event.x / col_size
        selected_row = 7 - (event.y / row_size)
        pos = self.chessboard.alpha_notation((selected_row, selected_column))
        try:
            piece = self.chessboard[pos]
        except:
            pass
        if self.selected_piece:
            self.shift(self.selected_piece[1], pos)
            self.selected_piece = None
            self.focused = None
            self.pieces = {}
            self.draw_board()
            self.draw_pieces()
        self.focus(pos)
        self.draw_board()
        
        

    def shift(self, p1, p2):
        piece = self.chessboard[p1]
        try:
            dest_piece = self.chessboard[p2]
        except:
            dest_piece = None
        if dest_piece is None or dest_piece.color != piece.color:
            try:
                self.chessboard.shift(p1,p2)
            except:
                pass

    def focus(self, pos):
        try:
            piece = self.chessboard[pos]
        except:
            piece=None
        if piece is not None and (piece.color == self.chessboard.player_turn):
            self.selected_piece = (self.chessboard[pos], pos)
            self.focused = map(self.chessboard.num_notation, (self.chessboard[pos].moves_available(pos)))

    def draw_board(self, event={}):
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.dim_square)
                y1 = ((7-row) * self.dim_square)
                x2 = x1 + self.dim_square
                y2 = y1 + self.dim_square
                if(self.focused is not None and (row, col) in self.focused):
                    self.canvas.create_rectangle(x1, y1, x2, y2,  fill=self.highlightcolor , tags="area")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2,  fill=color, tags="area")
                color = self.color1 if color == self.color2 else self.color2
        for name in self.pieces:
            self.pieces[name] = (self.pieces[name][0], self.pieces[name][1])
            x0 = (self.pieces[name][1] * self.dim_square) + int(self.dim_square/2)
            y0 = ((7-self.pieces[name][0]) * self.dim_square) + int(self.dim_square/2)
            self.canvas.coords(name, x0, y0)
        self.canvas.tag_raise("occupied")
        self.canvas.tag_lower("area")
        

    def draw_pieces(self):
        self.canvas.delete("occupied")
        for coord, piece in self.chessboard.iteritems():
            x,y = self.chessboard.num_notation(coord)
            if piece is not None:
                filename = "../pieces_image/%s%s.png" % (piece.shortname.lower(),piece.color)
                piecename = "%s%s%s" % (piece.shortname, x, y)
                if(filename not in self.images):
                    self.images[filename] = ImageTk.PhotoImage(file=filename)
                self.canvas.create_image(0,0, image=self.images[filename], tags=(piecename, "occupied"), anchor="c")
                x0 = (y * self.dim_square) + int(self.dim_square/2)
                y0 = ((7-x) * self.dim_square) + int(self.dim_square/2)
                self.canvas.coords(piecename, x0, y0)

        
def main(chessboard):
    root = Tk()
    root.title("Chess")
    gui = GUI(root, chessboard)
    gui.draw_board()
    gui.draw_pieces()
    root.mainloop()

if __name__ == "__main__":
    game = chessboard.Board()
    main(game)
