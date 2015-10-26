"""
Code illustration: 4.03
Displaying Pieces on the board

Tkinter GUI Application Development Hotshot
""" 

import sys

SHORT_NAME = { 'R':'Rook', 'N':'Knight', 'B':'Bishop', 'Q':'Queen', 'K':'King', 'P':'Pawn'}

def create_piece(piece, color='white'):
    ''' Takes a piece name or shortname and returns the corresponding piece instance '''
    if piece in (None, ' '): return
    if piece.isupper(): color = 'white'
    else: color = 'black'
    piece = SHORT_NAME[piece.upper()]
    module = sys.modules[__name__]
    return module.__dict__[piece](color)

class Piece():
    def __init__(self, color):
        if color == 'black':
            self.shortname = self.shortname.lower()
        elif color == 'white':
            self.shortname = self.shortname.upper()
        self.color = color


    def ref(self, board):
        ''' Get a reference of chess board instance'''
        self.board = board

class King(Piece):    shortname = 'k'
class Queen(Piece):    shortname = 'q'
class Rook(Piece):    shortname = 'r'
class Knight(Piece):    shortname = 'n'
class Bishop(Piece):    shortname = 'b'
class Pawn(Piece):     shortname = 'p'




