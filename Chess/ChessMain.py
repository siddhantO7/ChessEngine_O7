"""
This file is responsible for handling the user inputs, and it will show the current game state object.

"""

import pygame as p
from Chess import ChessEngine

# These are the global variables.
WIDTH = HEIGHT = 512  # 400 is also a good option.
DIMENSION = 8  # dimension of chess board are 8 x 8.
SQ_SIZE = HEIGHT // DIMENSION  # This stands for indivisual square size of chessboard.
MAX_FPS = 15  # For animation purpose & going to use it later on.
IMAGES = {}

'''
loadImages initialize a global dictionary of images. This will be called exactly once in the main.We 
are doing this because the as the game will proceed it will take more and more space and 
then the game will eventually lag. Hence we are calling it once in the main so much memory 
won't be needed.
'''


def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("Images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    # Note : We can access an image by saying 'IMAGES['wp']'


"""
The main driver for our code and this will handle the input and upadting the graphics.
"""


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()  # Only do this once, before the while loop
    running = True
    sqSelected = ()  # Keep track of the last click of the user. No square is selected initially. It's a tuple(row,column)
    playerClicks = []  # Keep track of the player clicks(two tuples : [(7,4), (5,4)])
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()  # This is the (x,y) location of the mouse
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sqSelected == (row, col):  # Checking if the user is clicking the same square after clicking any piece.
                    sqSelected = ()  # If the click is on same square as selected, then will clear selected square
                    playerClicks = []  # And will clear the next square clicked.
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)  # We append for both first and second clicks
                if len(playerClicks) == 2:  # After the 2nd click
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected = ()  # Reset the user clicks
                    playerClicks = []  #

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


"""
  Function drawGameState is responsible for all the graphics within a current game state.

"""


def drawGameState(screen, gs):
    drawBoard(screen)  # For drawing squares on the board.

    # Add in piece highlighter or move suggestions(Add later on)

    drawPieces(screen, gs.board)  # Draw pieces on top of those squares.


"""
Function drawBoard will draw the squares and the board on the screen. The top left square of chessboard is always light.
"""


def drawBoard(screen):
    colors = [p.Color("beige"), p.Color("limegreen")]  # first color is white and second color is black
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


"""
    Function drawPieces will draw the pieces on the board using the current GameState.board
"""


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":  # If not empty square
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
