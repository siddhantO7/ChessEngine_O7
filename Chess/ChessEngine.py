"""
This class is responsible for storing the current state of the game and also responsible for determining the
valid moves at the current state of the chess game. It will also keep a move log.

"""


class GameState():
    def __init__(self):
        # board is 8x8 2 dimensional list. Each element of the list has two characters. -- means empty space.
        # First letter stands for color of chess piece and second letter stands for chess piece.
        # So the pieces are "R", "N" , "B" , "Q" , "K" or "p".
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.WhiteToMove = True
        self.moveLog = []
