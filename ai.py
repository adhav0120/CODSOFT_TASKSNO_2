class TicTacToeAI:
    """
    Implements the Minimax decision algorithm with Alpha-Beta Pruning.
    Acts as the decision-making engine for the unbeatable Tic-Tac-Toe AI.
    """
    def __init__(self, ai_symbol, human_symbol):
        self.ai_symbol = ai_symbol
        self.human_symbol = human_symbol

    def minimax(self, board, depth, is_maximizing, alpha, beta):
        """
        Recursive Minimax search with Alpha-Beta Pruning.
        
        Parameters:
        - board: The Board object to evaluate.
        - depth: The current depth in the search tree.
        - is_maximizing: True if it's the AI's turn, False if it's the human's turn.
        - alpha: Lower bound score for the maximizing player.
        - beta: Upper bound score for the minimizing player.
        """
        # Base Cases (Terminal States)
        if board.check_win(self.ai_symbol):
            return 10 - depth
        if board.check_win(self.human_symbol):
            return -10 + depth
        if board.is_full():
            return 0

        # Recursive Cases
        if is_maximizing:
            max_eval = -float('inf')
            for move in board.get_available_moves():
                board.make_move(move, self.ai_symbol)
                evaluation = self.minimax(board, depth + 1, False, alpha, beta)
                board.undo_move(move)
                
                max_eval = max(max_eval, evaluation)
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break  # Beta cutoff (pruning)
            return max_eval
        else:
            min_eval = float('inf')
            for move in board.get_available_moves():
                board.make_move(move, self.human_symbol)
                evaluation = self.minimax(board, depth + 1, True, alpha, beta)
                board.undo_move(move)
                
                min_eval = min(min_eval, evaluation)
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break  # Alpha cutoff (pruning)
            return min_eval

    def get_best_move(self, board):
        """
        Determines the optimal move for the AI on a given board.
        """
        best_val = -float('inf')
        best_move = None
        alpha = -float('inf')
        beta = float('inf')
        
        for move in board.get_available_moves():
            board.make_move(move, self.ai_symbol)
            move_val = self.minimax(board, 0, False, alpha, beta)
            board.undo_move(move)
            
            if move_val > best_val:
                best_val = move_val
                best_move = move
                
        return best_move
