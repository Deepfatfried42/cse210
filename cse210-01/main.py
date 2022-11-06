"""Tic-Tac-Toe
   By Johnathon A Staples"""
import colorama
from colorama import Fore, Back, Style
colorama.init()

ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
X, O, = f'{Fore.BLUE}X', f'{Fore.RED}O',
BLANK = f'{Fore.GREEN}'

def main():
    print('Welcome to Tic-Tac-Toe.')
    gameBoard = BlankBoard()
    currentPlayer, nextPlayer = X, O

    while True:
        print(BoardStr(gameBoard))

        move = None
        while not ValidSpace(gameBoard, move):
            print('{}\'s move? (1-9)'.format(currentPlayer))
            move = input('> ')
        updateBoard(gameBoard, move, currentPlayer)

        if Winner(gameBoard, currentPlayer):
            print(BoardStr(gameBoard))
            print(currentPlayer + f'{Fore.YELLOW}WINNER!!!!')
            break
        elif BoardFull(gameBoard):
            print(BoardStr(gameBoard))
            print( f'{Fore.RED}The game is a DRAW!')
            break

        currentPlayer, nextPlayer = nextPlayer, currentPlayer
    print('Thanks for playing!')

def BlankBoard():
    """Create a new board."""
    board = {}
    for space in ALL_SPACES:
          board[space] = BLANK
    return board

def BoardStr(board):
    """Return a valid space on the board."""
    return '''
    {} |{}|{}  1 2 3
    -+-+-
    {} |{}|{}  4 5 6
    -+-+-
    {} |{}|{}  7 8 9'''.format(board['1'], board['2'], board['3'],
                               board['4'], board['5'], board['6'],
                               board['7'], board['8'], board['9'])

def ValidSpace(board, space):
    """Returns True if the space on the board is valid."""
    return space in ALL_SPACES and board[space] == BLANK

def Winner(board, player):
    """Return True if player is a winner."""

    b, p = board, player

    return ((b['1'] == b['2'] == b['3'] == p) or
            (b['4'] == b['5'] == b['6'] == p) or
            (b['7'] == b['8'] == b['9'] == p) or
            (b['1'] == b['4'] == b['7'] == p) or
            (b['2'] == b['5'] == b['8'] == p) or
            (b['3'] == b['6'] == b['9'] == p) or
            (b['3'] == b['5'] == b['7'] == p) or
            (b['1'] == b['5'] == b['9'] == p))

def BoardFull(board):
    """Return True if every space on the board has been taken."""
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False
    return True


def updateBoard(board, space, mark):
    """Update the board."""
    board[space] = mark


if __name__ == '__main__':
    main()
