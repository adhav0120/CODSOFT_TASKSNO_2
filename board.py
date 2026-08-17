class Board:
    """
    Encapsulates the Tic-Tac-Toe 3x3 board state and basic rules.
    """
    def __init__(self):
        # 0 | 1 | 2
        # --+---+--
        # 3 | 4 | 5
        # --+---+--
        # 6 | 7 | 8
        self.grid = [' ' for _ in range(9)]

    def print_board(self):
        """Prints the current board and the reference layout side-by-side."""
        print("\n      Current Board            Reference Grid")
        print(f"        {self.grid[0]} | {self.grid[1]} | {self.grid[2]}                1 | 2 | 3")
        print("       ---+---+---              ---+---+---")
        print(f"        {self.grid[3]} | {self.grid[4]} | {self.grid[5]}                4 | 5 | 6")
        print("       ---+---+---              ---+---+---")
        print(f"        {self.grid[6]} | {self.grid[7]} | {self.grid[8]}                7 | 8 | 9\n")

    def is_full(self):
        """Checks if there are no empty spaces remaining on the board."""
        return ' ' not in self.grid

    def check_win(self, player_symbol):
        """
        Determines if the specified player symbol has won the game.
        Checks all 8 possible winning combinations (rows, columns, diagonals).
        """
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for cond in win_conditions:
            if self.grid[cond[0]] == self.grid[cond[1]] == self.grid[cond[2]] == player_symbol:
                return True
        return False

    def get_available_moves(self):
        """Returns a list of board indexes (0-8) that are currently empty."""
        return [i for i, spot in enumerate(self.grid) if spot == ' ']

    def make_move(self, position, symbol):
        """Applies a player move to the board."""
        if self.grid[position] == ' ':
            self.grid[position] = symbol
            return True
        return False

    def undo_move(self, position):
        """Undoes a move at the specified position (used for backtracking)."""
        self.grid[position] = ' '
