import tkinter as tk
from tkinter import messagebox
from board import Board
from ai import TicTacToeAI

class TicTacToeGUI:
    """
    Tkinter Graphical User Interface for the unbeatable Tic-Tac-Toe AI.
    Features a modern dark theme and interactive state transitions.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Unbeatable Tic-Tac-Toe AI")
        self.root.geometry("400x520")
        self.root.resizable(False, False)
        
        # Color Palette (Modern Dark Theme)
        self.bg_dark = "#121212"       # Main background
        self.bg_panel = "#1E1E1E"      # Panel/Card background
        self.btn_normal = "#2D2D2D"    # Button normal state
        self.btn_hover = "#3D3D3D"     # Button hover state
        self.fg_white = "#E0E0E0"      # Standard text
        self.color_x = "#FF5C5C"       # Pastel red for X
        self.color_o = "#5C93FF"       # Pastel blue for O
        self.btn_action = "#00B4D8"    # Reset/Select buttons

        self.root.configure(bg=self.bg_dark)
        
        # Game State Variables
        self.board = None
        self.ai = None
        self.human_symbol = None
        self.ai_symbol = None
        self.current_turn = None
        self.buttons = []
        
        # Container frames
        self.main_container = tk.Frame(self.root, bg=self.bg_dark)
        self.main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Load Selection Screen
        self.show_selection_screen()

    def clear_container(self):
        """Helper to clear all widgets from the main container."""
        for widget in self.main_container.winfo_children():
            widget.destroy()

    def show_selection_screen(self):
        """Displays the initial symbol selection screen."""
        self.clear_container()
        
        # Title Label
        title_lbl = tk.Label(
            self.main_container,
            text="Tic-Tac-Toe AI",
            font=("Segoe UI", 26, "bold"),
            bg=self.bg_dark,
            fg=self.fg_white
        )
        title_lbl.pack(pady=(40, 10))

        subtitle_lbl = tk.Label(
            self.main_container,
            text="Unbeatable Minimax Algorithm",
            font=("Segoe UI", 12, "italic"),
            bg=self.bg_dark,
            fg="#888888"
        )
        subtitle_lbl.pack(pady=(0, 40))

        prompt_lbl = tk.Label(
            self.main_container,
            text="Choose your symbol (X goes first):",
            font=("Segoe UI", 12),
            bg=self.bg_dark,
            fg=self.fg_white
        )
        prompt_lbl.pack(pady=10)

        # Buttons Frame
        btn_frame = tk.Frame(self.main_container, bg=self.bg_dark)
        btn_frame.pack(pady=20)

        btn_x = tk.Button(
            btn_frame,
            text="Play as X",
            font=("Segoe UI", 12, "bold"),
            bg=self.color_x,
            fg=self.bg_dark,
            activebackground="#D43F3F",
            activeforeground=self.bg_dark,
            width=12,
            height=2,
            bd=0,
            cursor="hand2",
            command=lambda: self.start_game("X")
        )
        btn_x.pack(side="left", padx=10)

        btn_o = tk.Button(
            btn_frame,
            text="Play as O",
            font=("Segoe UI", 12, "bold"),
            bg=self.color_o,
            fg=self.bg_dark,
            activebackground="#4A7BD0",
            activeforeground=self.bg_dark,
            width=12,
            height=2,
            bd=0,
            cursor="hand2",
            command=lambda: self.start_game("O")
        )
        btn_o.pack(side="left", padx=10)

    def start_game(self, symbol):
        """Transitions to the game screen and initializes state."""
        self.human_symbol = symbol
        self.ai_symbol = "O" if symbol == "X" else "X"
        self.current_turn = "X"  # X always plays first
        
        self.board = Board()
        self.ai = TicTacToeAI(self.ai_symbol, self.human_symbol)
        
        self.show_game_screen()
        
        # If AI is X, AI plays first move
        if self.ai_symbol == "X":
            self.set_status("AI is thinking...")
            self.root.after(500, self.trigger_ai_move)

    def show_game_screen(self):
        """Constructs the 3x3 grid and status labels."""
        self.clear_container()
        self.buttons = []

        # Status Bar Panel
        self.status_lbl = tk.Label(
            self.main_container,
            text=f"Your Turn ({self.human_symbol})" if self.current_turn == self.human_symbol else "AI is thinking...",
            font=("Segoe UI", 14, "bold"),
            bg=self.bg_dark,
            fg=self.fg_white
        )
        self.status_lbl.pack(pady=(10, 20))

        # 3x3 Grid Frame
        grid_frame = tk.Frame(self.main_container, bg=self.bg_dark)
        grid_frame.pack()

        # Build grid buttons
        for i in range(9):
            row = i // 3
            col = i % 3
            
            btn = tk.Button(
                grid_frame,
                text="",
                font=("Segoe UI", 24, "bold"),
                bg=self.btn_normal,
                activebackground=self.btn_hover,
                bd=0,
                width=5,
                height=2,
                cursor="hand2",
                command=lambda pos=i: self.handle_click(pos)
            )
            btn.grid(row=row, column=col, padx=4, pady=4)
            
            # Setup hover animations
            btn.bind("<Enter>", lambda e, b=btn: self.on_enter(b))
            btn.bind("<Leave>", lambda e, b=btn: self.on_leave(b))
            
            self.buttons.append(btn)

        # Footer Frame (Restart Button)
        footer_frame = tk.Frame(self.main_container, bg=self.bg_dark)
        footer_frame.pack(pady=25)

        restart_btn = tk.Button(
            footer_frame,
            text="Back to Menu",
            font=("Segoe UI", 10, "bold"),
            bg=self.btn_normal,
            fg=self.fg_white,
            activebackground=self.btn_hover,
            activeforeground=self.fg_white,
            width=14,
            height=2,
            bd=0,
            cursor="hand2",
            command=self.show_selection_screen
        )
        restart_btn.pack()

    def set_status(self, text):
        """Updates status text."""
        self.status_lbl.config(text=text)

    def on_enter(self, btn):
        """Hover enter effect."""
        if btn["state"] == "normal":
            btn.config(bg=self.btn_hover)

    def on_leave(self, btn):
        """Hover leave effect."""
        if btn["state"] == "normal":
            btn.config(bg=self.btn_normal)

    def handle_click(self, position):
        """Processes human move clicks."""
        if self.current_turn != self.human_symbol:
            return  # Ignore clicks during AI turn
            
        # Perform move
        if self.board.make_move(position, self.human_symbol):
            self.update_button(position, self.human_symbol)
            
            # Check terminal state
            if self.check_game_over():
                return

            # Turn switches to AI
            self.current_turn = self.ai_symbol
            self.set_status("AI is thinking...")
            self.disable_board()
            
            # Simulated AI thinking time for realistic UX
            self.root.after(400, self.trigger_ai_move)

    def trigger_ai_move(self):
        """Invokes the AI engine to evaluate and perform the best move."""
        best_move = self.ai.get_best_move(self.board)
        if best_move is not None:
            self.board.make_move(best_move, self.ai_symbol)
            self.update_button(best_move, self.ai_symbol)
            
            if self.check_game_over():
                return
            
            # Turn switches back to human
            self.current_turn = self.human_symbol
            self.set_status(f"Your Turn ({self.human_symbol})")
            self.enable_board()

    def update_button(self, position, symbol):
        """Updates grid button text and color state."""
        color = self.color_x if symbol == "X" else self.color_o
        btn = self.buttons[position]
        btn.config(
            text=symbol,
            fg=color,
            bg=self.btn_normal,
            state="disabled",
            disabledforeground=color
        )

    def disable_board(self):
        """Disables clicks on empty cells."""
        for i in self.board.get_available_moves():
            self.buttons[i].config(state="disabled")

    def enable_board(self):
        """Enables clicks on empty cells."""
        for i in self.board.get_available_moves():
            self.buttons[i].config(state="normal", bg=self.btn_normal)

    def check_game_over(self):
        """Scans board state and shows alert dialogs if terminal."""
        if self.board.check_win(self.human_symbol):
            self.set_status("You Won!")
            messagebox.showinfo("Game Over", "Congratulations! You won!")
            self.show_selection_screen()
            return True
            
        if self.board.check_win(self.ai_symbol):
            self.set_status("AI Wins!")
            messagebox.showinfo("Game Over", "Game Over! The AI won.")
            self.show_selection_screen()
            return True
            
        if self.board.is_full():
            self.set_status("Tie Game!")
            messagebox.showinfo("Game Over", "It's a Tie! Perfect game.")
            self.show_selection_screen()
            return True
            
        return False
