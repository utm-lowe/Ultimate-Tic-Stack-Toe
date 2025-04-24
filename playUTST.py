#!/usr/bin/env python3
from ticTacToe import UltimateTicStackToeBoard
from agent import get_players

def board_strings(board):
    result = []
    for r in range(3):
        row = board.grid[r]
        row = [cell.winner if cell.winner is not None else ' ' for cell in row]
        result.append(' ' + " | ".join(row)+' ')
        if r != 2:
            result.append("---+---+---")
    return result

def print_utt_board(board):
    """
    Print the board to the console.
    """
    bigX = [ "   X    X  ",
             "    X  X   ",
             "     XX    ",
             "    X  X   ", 
             "   X    X  " ] 

    bigO = [ "  OOOOOO   ",
             " O      O  ",
             " O      O  ",
             " O      O  ",
             "  OOOOOO   " ]

    for by in range(3):
        row = []
        for bx in range(3):
            if board.grid[by][bx].winner == 'X':
                row.append(bigX)
            elif board.grid[by][bx].winner == 'O':
                row.append(bigO)
            else:
                row.append(board_strings(board.grid[by][bx]))
        for srow in range(len(row[0])):
            print(" # ".join([r[srow] for r in row]))
        if by != 2:
            print("#"*39)

def print_board(board):
    for board in board.boards:
        print_utt_board(board)
        print()

board = UltimateTicStackToeBoard()

player='X'

players = get_players('layer, bx, by, x, y')

while board.winner is None:
    try:
        print_board(board)
        move=players[player].get_move(board)
        board.move(*move,player)
        print()
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
    except KeyboardInterrupt:
        break
    except Exception as e:
        print("Invalid move, please try again.")
        print(e)

print_board(board)
print("Winner: " + str(board.winner))
