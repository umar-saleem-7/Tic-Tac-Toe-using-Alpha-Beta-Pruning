# Tic-Tac-Toe with Alpha-Beta Pruning

This project implements a *Tic-Tac-Toe* game using Python's *Tkinter* library for the graphical user interface (GUI) and the *Alpha-Beta Pruning algorithm* for the computer's decision-making process. Players can choose to play against a friend or the computer, with the computer's moves optimized using a minimax strategy enhanced by alpha-beta pruning.

---

## Features

- *Two Game Modes*:
  - Play against the *computer* (AI).
  - Play against a *friend* in a local two-player mode.
  
- *Intelligent AI*:
  - The computer uses the *Alpha-Beta Pruning algorithm* to make optimal moves, ensuring challenging gameplay.

- *Interactive GUI*:
  - Built with *Tkinter*, the game features a responsive and user-friendly interface.
  
- *Dynamic Gameplay*:
  - Randomized first turn between the player and the computer.
  - Highlighted buttons for each player's move with distinct colors:
    - *Blue* for Player O.
    - *Red* for Player X.

- *Reset and Navigation*:
  - Easily restart the game with the *Reset* button.
  - Navigate back to the main menu using the *Back* button.

---

## Installation and Usage

### Prerequisites
Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository
bash
git clone https://github.com/umar-saleem-7/Tic-Tac-Toe-using-Alpha-Beta-Pruning.git
cd tic-tac-toe-alpha-beta


### Install Dependencies
This project uses only the built-in *Tkinter* module. No additional installations are required.

### Run the Game
Run the following command in the terminal:
bash
python tic_tac_toe.py


---

## How to Play

1. *Start the Game*:
   - Launch the game and select a mode:
     - Play against the *Computer*.
     - Play with a *Friend*.

2. *Make Moves*:
   - Click on any empty cell to place your marker (*O* or *X*).
   - The AI will automatically make its move in the single-player mode.

3. *Game Over*:
   - A winner is declared when three markers align horizontally, vertically, or diagonally.
   - If all cells are filled without a winner, the game ends in a *draw*.

4. *Reset or Exit*:
   - Use the *Reset* button to restart the game.
   - Use the *Back* button to return to the main menu.

---

## Algorithm Details

The computer's decision-making uses the *Alpha-Beta Pruning* algorithm:
- It evaluates the best possible move for the computer (Player X) while minimizing the opponent's chances of winning.
- The algorithm explores the game tree more efficiently by pruning branches that won't affect the outcome, ensuring faster decisions.

---

