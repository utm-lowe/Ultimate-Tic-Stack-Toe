#!/usr/bin/env python3
from ticTacToe import TicTacToe3dBoard
from agent import get_players

def print_board(board):
    """
    Print the board to the console.
    """
    for bi in range(3):
        for r in range(3):
            row = board.boards[bi].grid[r]
            row = [cell.winner if cell.winner is not None else ' ' for cell in row]
            print(' ' + " | ".join(row))
            if r != 2:
                print("---+---+---")
        print("\n")

board = TicTacToe3dBoard()

player='X'

players = get_players('layer, x, y')

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
