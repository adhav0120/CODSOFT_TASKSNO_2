#!/usr/bin/env python3
"""
Task 2: Tic-Tac-Toe AI
Lightweight entry point to launch the unbeatable Tic-Tac-Toe game.
By default, launches the Tkinter-based Windows Desktop GUI.
Supports a `--cli` flag to launch the text-based console interface instead.

Usage:
  python tic_tac_toe.py        # Launches GUI (default)
  python tic_tac_toe.py --cli  # Launches CLI
"""

import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Unbeatable Tic-Tac-Toe AI")
    parser.add_argument("--cli", action="store_true", help="Launch the text-based console interface")
    args = parser.parse_args()

    if args.cli:
        from game import TicTacToeGame
        try:
            game = TicTacToeGame()
            game.start()
        except KeyboardInterrupt:
            print("\n\nGame terminated. Goodbye!")
            sys.exit(0)
    else:
        try:
            import tkinter as tk
            from gui import TicTacToeGUI
        except ImportError as e:
            print(f"Error: Could not load GUI dependencies ({e}). Falling back to CLI mode...")
            from game import TicTacToeGame
            game = TicTacToeGame()
            game.start()
            return
            
        root = tk.Tk()
        app = TicTacToeGUI(root)
        root.mainloop()

if __name__ == "__main__":
    main()
