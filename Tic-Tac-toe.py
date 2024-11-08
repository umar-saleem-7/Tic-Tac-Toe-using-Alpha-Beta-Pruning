import time 
import tkinter as tk
from tkinter import messagebox
import random

class AlphaBeta:
    def __init__(self, game_state):
        self.game_state = game_state

    def is_terminal(self, state):
        win_conditions = [((0, 0), (0, 1), (0, 2)),  # Rows
                          ((1, 0), (1, 1), (1, 2)),
                          ((2, 0), (2, 1), (2, 2)),
                          ((0, 0), (1, 0), (2, 0)),  # Columns
                          ((0, 1), (1, 1), (2, 1)),
                          ((0, 2), (1, 2), (2, 2)),
                          ((0, 0), (1, 1), (2, 2)),  # Diagonals
                          ((0, 2), (1, 1), (2, 0))]
        for condition in win_conditions:
            if state[condition[0][0]][condition[0][1]] == state[condition[1][0]][condition[1][1]] == state[condition[2][0]][condition[2][1]] and state[condition[0][0]][condition[0][1]] != ' ':
                return True
        return False

    def utility(self, state):
        win_conditions = [((0, 0), (0, 1), (0, 2)),
                          ((1, 0), (1, 1), (1, 2)),
                          ((2, 0), (2, 1), (2, 2)),
                          ((0, 0), (1, 0), (2, 0)),
                          ((0, 1), (1, 1), (2, 1)),
                          ((0, 2), (1, 2), (2, 2)),
                          ((0, 0), (1, 1), (2, 2)),
                          ((0, 2), (1, 1), (2, 0))]
        for condition in win_conditions:
            if state[condition[0][0]][condition[1][0]] == 'X':
                return 1
            elif state[condition[0][0]][condition[1][0]] == 'O':
                return -1
        return 0

    def alpha_beta(self, state, depth, alpha, beta, maximizing_player):
        if self.is_terminal(state):
            return self.utility(state)

        if maximizing_player:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if state[i][j] == ' ':
                        state[i][j] = 'X'
                        score = self.alpha_beta(state, depth + 1, alpha, beta, False)
                        state[i][j] = ' '
                        best_score = max(score, best_score)
                        alpha = max(alpha, best_score)
                        if beta <= alpha:
                            break
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if state[i][j] == ' ':
                        state[i][j] = 'O'
                        score = self.alpha_beta(state, depth + 1, alpha, beta, True)
                        state[i][j] = ' '
                        best_score = min(score, best_score)
                        beta = min(beta, best_score)
                        if beta <= alpha:
                            break
            return best_score

    def best_move(self, state):
        # Check if the computer has a winning move first
        for i in range(3):
            for j in range(3):
                if state[i][j] == ' ':
                    state[i][j] = 'X'  # Assume computer is 'X'
                    if self.is_terminal(state):
                        state[i][j] = ' '  # Undo move
                        return (i, j)  # Return winning move
                    state[i][j] = ' '  # Undo move

        # If no winning move, check if the player has a winning move to block
        for i in range(3):
            for j in range(3):
                if state[i][j] == ' ':
                    state[i][j] = 'O'  # Assume player is 'O'
                    if self.is_terminal(state):
                        state[i][j] = ' '  # Undo move
                        return (i, j)  # Block player’s winning move
                    state[i][j] = ' '  # Undo move

        # If no immediate win or block, use alpha-beta search for the best move
        best_score = -float('inf')
        move = (-1, -1)
        alpha = -float('inf')
        beta = float('inf')
        for i in range(3):
            for j in range(3):
                if state[i][j] == ' ':
                    state[i][j] = 'X'
                    score = self.alpha_beta(state, 0, alpha, beta, False)
                    state[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move



class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe Game")
        self.root.geometry("400x450")
        self.root.config(bg="#2c3e50")  # Darker background color

        self.game_state = [[' ' for _ in range(3)] for _ in range(3)]
        self.alpha_beta = AlphaBeta(self.game_state)

        self.current_player = 'O'
        self.two_player_mode = False
        self.play_button = None

        self.show_play_button()

    def show_play_button(self):
        self.play_button = tk.Button(self.root, text="Play", font=("Arial Bold", 16), bg="#34495e", fg="white", command=self.show_menu)
        self.play_button.place(relx=0.5, rely=0.5, anchor="center")

    def show_menu(self):
        self.play_button.destroy()
        self.play_mode_label = tk.Label(self.root, text="Select Mode", font=("Arial", 14), bg="lightgray")
        self.play_mode_label.place(relx=0.5, rely=0.3, anchor="center")

        self.play_with_computer_button = tk.Button(self.root, text="Play with Computer", font=("Arial", 12), bg="#333333", fg="white", command=lambda: self.set_mode(False))
        self.play_with_computer_button.place(relx=0.5, rely=0.4, anchor="center")
        self.play_with_friend_button = tk.Button(self.root, text="Play with Friend", font=("Arial", 12), bg="#333333", fg="white", command=lambda: self.set_mode(True))
        self.play_with_friend_button.place(relx=0.5, rely=0.5, anchor="center")

        self.back_button = tk.Button(self.root, text="Back", font=("Arial", 12), bg="#333333", fg="white", command=self.back_to_main)
        self.back_button.place(relx=0.5, rely=0.6, anchor="center")

    def set_mode(self, two_player):
        self.two_player_mode = two_player
        self.start_game()

    def back_to_main(self):
        if hasattr(self, 'buttons'):
            for row in self.buttons:
                for button in row:
                    button.destroy()
            self.reset_button.destroy()
            self.back_button.destroy()
        else:
            self.play_with_computer_button.destroy()
            self.play_with_friend_button.destroy()
            self.play_mode_label.destroy()
            self.back_button.destroy()
        self.show_play_button()

    def start_game(self):
        self.play_with_computer_button.destroy()
        self.play_with_friend_button.destroy()
        self.play_mode_label.destroy()
        self.back_button.destroy()
        self.create_board()

        self.current_player = random.choice(['O', 'X'])
    
        # If computer is selected to go first
        if self.current_player == 'X' and not self.two_player_mode:
            self.computer_move()

    def create_board(self):
        frame = tk.Frame(self.root, bg="#2c3e50")
        frame.place(relx=0.5, rely=0.5, anchor="center", y=-50)

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(frame, text="", font=("Arial Bold", 18), width=5, height=2,
                                   bg="#3498db", fg="white",  # Change button colors
                                   command=lambda i=i, j=j: self.player_move(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.reset_button = tk.Button(self.root, text="Reset", font=("Arial Bold", 12), bg="#e74c3c", fg="white", command=self.reset_game)
        self.reset_button.place(relx=0.3, rely=0.9, anchor="center")

        self.back_button = tk.Button(self.root, text="Back", font=("Arial Bold", 12), bg="#e74c3c", fg="white", command=self.back_to_main)
        self.back_button.place(relx=0.7, rely=0.9, anchor="center")


    def player_move(self, row, col):
        if self.game_state[row][col] == ' ':
            color = "blue" if self.current_player == 'O' else "red"
            self.game_state[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, fg=color)

            if self.alpha_beta.is_terminal(self.game_state):
                self.show_winner(f"{'You' if self.current_player == 'O' else 'Computer'} win!" if not self.two_player_mode else f"Player {2 if self.current_player == 'X' else 1} wins!")
                return
            if all(cell != ' ' for row in self.game_state for cell in row):
                self.show_winner("Draw!")
                return

            if self.two_player_mode:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
            else:
                self.current_player = 'X'
                self.computer_move()

    def computer_move(self):
        move = self.alpha_beta.best_move(self.game_state)
        if move != (-1, -1):
            row, col = move
            self.game_state[row][col] = 'X'
            self.buttons[row][col].config(text='X', fg="red")
            if self.alpha_beta.is_terminal(self.game_state):
                self.show_winner("Computer wins!")
                return
            if all(cell != ' ' for row in self.game_state for cell in row):
                self.show_winner("Draw!")
                return
            self.current_player = 'O'

    def show_winner(self, message):
        messagebox.showinfo("Game Over", message)
        self.reset_game()

    def reset_game(self):
        for row in self.buttons:
            for button in row:
                button.config(text="", fg="white")
        self.game_state = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'O'


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
