import sys
from board import Board
from ai import TicTacToeAI

class TicTacToeGame:
    """
    Manages the game controller, player input, and main turn loop.
    """
    def __init__(self):
        self.board = Board()
        self.human_symbol = None
        self.ai_symbol = None
        self.ai = None

    def start(self):
        """Main game loop for CLI interaction."""
        print("=" * 60)
        print("          WELCOME TO UNBEATABLE TIC-TAC-TOE AI          ")
        print("=" * 60)
        print("The AI uses the Minimax algorithm with Alpha-Beta Pruning.")
        print("It cannot be beaten! The best possible outcome is a draw.")
        print("=" * 60)
        
        # 1. Let the player select their symbol
        while True:
            choice = input("Do you want to play as X (goes first) or O (goes second)? [X/O]: ").strip().upper()
            if choice in ['X', 'O']:
                self.human_symbol = choice
                self.ai_symbol = 'O' if choice == 'X' else 'X'
                break
            print("Invalid input. Please enter 'X' or 'O'.")

        # Instantiate AI with its and human's symbol
        self.ai = TicTacToeAI(self.ai_symbol, self.human_symbol)

        # 2. Determine who goes first based on standard rules (X goes first)
        current_turn = 'X'
        
        print(f"\nGame started! You are '{self.human_symbol}' and the AI is '{self.ai_symbol}'.")
        self.board.print_board()

        # 3. Game loop
        while True:
            # Check terminal state
            if self.board.check_win(self.human_symbol):
                print("Congratulations! You won! (Wait, how did you beat an unbeatable AI?!)")
                break
            elif self.board.check_win(self.ai_symbol):
                print("Game Over! The AI won. Nice try!")
                break
            elif self.board.is_full():
                print("It's a Tie! A perfect game.")
                break

            # Handle moves
            if current_turn == self.human_symbol:
                # Human Turn
                while True:
                    try:
                        move_input = input(f"Your turn ({self.human_symbol}). Enter a position (1-9): ").strip()
                        position = int(move_input) - 1
                        
                        if position < 0 or position > 8:
                            print("Out of bounds. Choose a number between 1 and 9.")
                            continue
                        
                        # Apply move (will fail and return False if occupied)
                        if not self.board.make_move(position, self.human_symbol):
                            print("That cell is already occupied. Choose another spot.")
                            continue
                        break
                    except ValueError:
                        print("Invalid input. Please enter an integer between 1 and 9.")
                
                # Switch turn
                current_turn = self.ai_symbol
            else:
                # AI Turn
                print(f"AI's turn ({self.ai_symbol}). Calculating best move...")
                best_move = self.ai.get_best_move(self.board)
                if best_move is not None:
                    self.board.make_move(best_move, self.ai_symbol)
                    print(f"AI chose position {best_move + 1}.")
                
                # Switch turn
                current_turn = self.human_symbol

            # Render board state
            self.board.print_board()

if __name__ == '__main__':
    try:
        game = TicTacToeGame()
        game.start()
    except KeyboardInterrupt:
        print("\n\nGame terminated. Goodbye!")
        sys.exit(0)
