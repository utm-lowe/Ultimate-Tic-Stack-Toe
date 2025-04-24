def has_win(l):
    """
    Check to see if the specified list l is a winner
    (filled with the same non-space)
    """
    return l[0] is not None and len(set(l)) == 1 


class TicTacToeElement:
    """
    A TicTacToeElement represents a single element in the Tic Tac Toe
    game. This could be a board, cell, or collection of boards. The
    defining chracteristic is that it has a 'winner' attribute that
    starts out as none.
    """
    def __init__(self):
        self.winner = None

    def to_dict(self):
        """
        Return a dictionary representation of the board. This is
        useful for serialization.
        """
        return {'winner': self.winner}

class TicTacToeCell(TicTacToeElement):
    """
    This is an individual cell in a tic-tac-toe board. When a player
    moves on this cell, the cell's winner is set to the player who moved.
    """
    def __init__(self):
        super().__init__()

    def move(self, player):
        """
        Make the move, provided the cell is empty. If the cell is
        occupied, raise an exception.
        """
        if self.winner is not None:
            raise Exception("Cell already occupied")
        self.winner = player

    def moves(self):
        """
        Return a list of move tuples. For an empty cell, this is just
        a single empty tuple. For a cell with a winner, this is an
        empty list.
        """

        if self.winner is not None:
            return []
        else:
            return [()]

class TicTacToeBoard(TicTacToeElement):
    """
    This is a basic tic-tac-toe board with its 9 elements. It checks
    for winners in the usual row, column, and diagonal ways.
    """
    def __init__(self, elementClass=TicTacToeCell):
        """
        Create a new board with 9 empty cells.
        """
        super().__init__()

        # make a 3x3 grid of elements
        self.grid = [[elementClass() for _ in range(3)] for _ in range(3)]

    def update_winner(self):
        """
        Update the field winner to one of the following:
          None - No winner
          'X' - X wins
          'O' - O wins
          'S' - Scratch / Tie
        """
        
        #check each row
        for row in self.grid:
            row = [c.winner for c in row]
            if has_win(row):
                self.winner=row[0]
                return
        
        #check each column
        for x in range(len(self.grid[0])):
            col = [self.grid[i][x].winner for i in range(len(self.grid))]
            if has_win(col):
                self.winner=col[0]
                return
        
        #check the diagonals
        diag = [[self.grid[i][i].winner for i in range(len(self.grid))], 
                [self.grid[i][len(self.grid)-i-1].winner for i in range(len(self.grid))]]
        for d in diag:
            if has_win(d):
                self.winner=d[0]
                return
        
        #check for open game
        for row in self.grid:
            for c in row:
                if c.winner is None:
                    return
        
        # must be a scratch
        self.winner='S'


    def moves(self):
        """
        Return a list of legal moves for the grid. This is our x,
        y coordinates combined with whatever cooridnates we have from
        lower order elements. (x,y,containng...)
        """
        # start with an empty list
        result = []

        # if we have winner, we have no moves
        if self.winner is not None:
            return result

        # loop over each cell
        for x in range(3):
            for y in range(3):
                cell = self.grid[y][x]

                # get the moves from the cell
                moves = cell.moves()

                # add the x,y to each move
                for m in moves:
                    result.append((x,y) + m)
        return result


    def move(self, x, y, *elementArgs):
        """
        Make a move at the specified x,y coordinate and update the
        winner.
        """
        cell = self.grid[y][x]
        cell.move(*elementArgs)
        self.update_winner()

    def to_dict(self):
        """
        Return a dictionary representation of the board. This is
        useful for serialization.
        """
        return {
            'winner': self.winner,
            'grid': [[cell.to_dict() for cell in row] for row in self.grid]
        }


class TicTacToe3dBoard(TicTacToeElement):
    """
    This is a 3D tic-tac-toe board with 27 elements. It checks
    for winners in the usual row, column, and diagonal ways, but with
    stacked boards.
    """
    def __init__(self, elementClass=TicTacToeCell, boardClass=TicTacToeBoard):
        super().__init__()

        # make the 3 boards
        self.boards = [boardClass(elementClass=elementClass) for _ in range(3)]

    def move(self, boardIndex, *elementArgs):
        """
        Make a move at the specified boardIndex,elementArgs coordinate and
        update the winner.
        """
        board = self.boards[boardIndex]
        board.move(*elementArgs)
        self.update_winner()

    def moves(self):
        """
        Return a list of legal moves for our 3d board.
        """

        result = []
        for boardIndex in range(3):
            # get the moves from the board
            moves = self.boards[boardIndex].moves()

            # add the z coordinate to each move
            for m in moves:
                result.append((boardIndex,) + m)
        return result

    def update_winner(self):
        # check for a winner among the boards
        for board in self.boards:
            if board.winner is not None and board.winner != 'S':
                self.winner = board.winner
                return

        #check for scratch
        if all(board.winner == 'S' for board in self.boards):
            self.winner = 'S'
            return

        # Check vertical wins across boards
        for x in range(3):
            for y in range(3):
                vert = [self.boards[z].grid[y][x].winner for z in range(3)]
                if has_win(vert):
                    self.winner = vert[0]
                    return

        # Check 3D diagonals
        ncells = len(self.boards)
        diag = [[self.boards[i].grid[i][i].winner for i in range(ncells)], 
                [self.boards[i].grid[i][ncells-i-1].winner for i in range(ncells)]]

        for c in range(ncells):
            diag.append([self.boards[i].grid[c][i].winner for i in range(ncells)])
            diag.append([self.boards[i].grid[c][ncells-i-1].winner for i in range(ncells)])
            diag.append([self.boards[i].grid[i][c].winner for i in range(ncells)])
            diag.append([self.boards[i].grid[ncells-i-1][c].winner for i in range(ncells)])

        for d in diag:
            if has_win(d):
                self.winner = d[0]
                return

    def to_dict(self):
        """
        Return a dictionary representation of the board. This is
        useful for serialization.
        """
        return {
            'winner': self.winner,
            'boards': [board.to_dict() for board in self.boards]
        }


class UltimateTicTacToeBoard(TicTacToeBoard):
    """
    This is an Ultimate Tic Tac Toe board with 9 boards. It checks
    for winners in the usual row, column, and diagonal ways, but with
    stacked boards.
    """
    def __init__(self, elementClass=TicTacToeBoard):
        super().__init__(elementClass=elementClass)
        self.last_board = None


    def moves(self):
        trial_moves = super().moves()
        result = []
        for move in trial_moves:
            # check if the move is valid
            if self.validate_board(move[0], move[1]):
                result.append(move)
        return result


    def move(self, bx, by, *elementArgs):
        """
        Make a move at the specified boardIndex,elementArgs coordinate and
        update the winner.
        """
        # validate the move
        if self.winner is not None:
            raise Exception("Board already won")
        if not self.validate_board(bx, by):
            raise Exception("Invalid board")

        # perform the move
        self.last_board=elementArgs[-3:-1]
        board = self.grid[by][bx]
        board.move(*elementArgs)
        self.update_winner()


    def validate_board(self, bx, by):
        """
        Return true if we can move on this board.
        """
        
        # we can't move onto an occupied/full board
        if self.grid[by][bx].winner is not None:
            return False

        # if we do not have a last move, we can move anywhere
        if self.last_board is None:
            return True
       
        # get the cooridnates of the last board
        lx,ly = self.last_board

        # if the last move is full, we can move anywhere
        if self.grid[ly][lx].winner is not None:
            return True 

        # if the last move is not full, we can only move on the
        # specified board
        return bx == lx and by == ly

    def to_dict(self):
        """
        Return a dictionary representation of the board. This is
        useful for serialization.
        """
        return {
            'winner': self.winner,
            'grid': [[cell.to_dict() for cell in row] for row in self.grid],
            'last_board': self.last_board
        }


class UltimateTicStackToeBoard(TicTacToe3dBoard):
    """
    This is an Ultimate Tic Tac Toe board with 9 boards. It checks
    for winners in the usual row, column, and diagonal ways, but with
    stacked boards.
    """
    def __init__(self):
        super().__init__(elementClass=TicTacToeBoard, boardClass=UltimateTicTacToeBoard)
        self.last_board = None
